import pika
import grpc
from mensagem_pb2 import Comando
from mensagem_pb2_grpc import LampadaServiceStub

def callback(channel, method, properties, body):
    comando = str(body, 'utf-8')
    print(f"Recebi a mensagem do RabbitMQ: {body}")

    # Configurar gRPC para enviar mensagens
    channel_grpc = grpc.insecure_channel('localhost:50053')
    stub = LampadaServiceStub(channel_grpc)

    # Enviar mensagem ao serviço gRPC
    resposta = stub.EnviarComando(Comando(comando = comando))
    print(f"Resposta do Servidor gRPC: {resposta.comando}")

def configurar_rabbitMQ_para_receber_mensagens():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return channel

def processar(channel):
    channel.queue_declare(queue='fila_sensor_presenca')
    channel.basic_consume(
        queue='fila_sensor_presenca',
        on_message_callback=callback,
        auto_ack=True
    )
    channel.start_consuming()

if __name__ == '__main__':
    channel_rabbitmq = configurar_rabbitMQ_para_receber_mensagens()
    processar(channel_rabbitmq)
