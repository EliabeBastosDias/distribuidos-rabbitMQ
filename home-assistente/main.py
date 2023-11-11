import pika
import grpc
from mensagem_pb2 import Comando
from mensagem_pb2_grpc import ArCondicionadoServiceStub

def callback(channel, method, properties, body):
    print(f"Recebi a mensagem do RabbitMQ: {body}")

    temperature = int(body)
    comando = 'N'
    if (30 < temperature <= 40):
        comando = 'S'

    # Configurar gRPC para enviar mensagens
    channel_grpc = grpc.insecure_channel('localhost:50051')
    stub = ArCondicionadoServiceStub(channel_grpc)

    # Enviar mensagem ao serviço gRPC
    resposta = stub.EnviarComando(Comando(comando = comando))
    print(f"Resposta do Servidor gRPC: {resposta.comando}")

def configurar_rabbitMQ_para_receber_mensagens():
    connection = pika.BlockingConnection(pika.ConnectionParameters('docker_rabbitmq', port=5672))
    channel = connection.channel()
    return channel

def configurar_grpc_para_enviar_mensagens():
    channel_grpc = grpc.insecure_channel('localhost:50051')
    stub = ArCondicionadoServiceStub(channel_grpc)
    return stub

def processar(channel):
    channel.queue_declare(queue='fila_sensor_temperatura')
    channel.basic_consume(
        queue='fila_sensor_temperatura',
        on_message_callback=callback,
        auto_ack=True
    )
    channel.start_consuming()

if __name__ == '__main__':
    channel_rabbitmq = configurar_rabbitMQ_para_receber_mensagens()
    processar(channel_rabbitmq)
