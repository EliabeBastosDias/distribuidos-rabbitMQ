import pika
import random
import time

def configurar_sensor_temperatura_rabbitMQ():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fila_sensor_temperatura')
    return channel

def mandar_mensagem(channel, mensagem):
    channel.basic_publish(
        exchange='',
        routing_key='fila_sensor_temperatura',
        body=mensagem
    )
    print("Mensagem enviada")

if __name__ == '__main__':
    channel = configurar_sensor_temperatura_rabbitMQ()
    while (True):
        temperatura = random.randint(10, 40)
        print(f"Temperatura: {temperatura}")
        if (temperatura <= 30):
            mandar_mensagem(channel, str(temperatura))
        time.sleep(5)