import pika
import random
import time

def configurar_sensor_fumaca_rabbitMQ():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fila_sensor_fumaca')
    return channel

def mandar_mensagem(channel, mensagem):
    channel.basic_publish(
        exchange='',
        routing_key='fila_sensor_fumaca',
        body=mensagem
    )
    print("Mensagem enviada")

if __name__ == '__main__':
    channel = configurar_sensor_fumaca_rabbitMQ()
    while (True):
        fumaca = random.randint(0, 1)

        if (fumaca):
            print(f"Fumaca: {fumaca}")
            mandar_mensagem(channel, "S")
        else:
            print(f"Fumaca: {fumaca}")
            mandar_mensagem(channel, "N")
        
        
        time.sleep(5)