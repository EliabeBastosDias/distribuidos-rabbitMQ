import pika
import random
import time

def configurar_sensor_temperatura_rabbitMQ():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fila_sensor_presenca')
    return channel

def mandar_mensagem(channel, mensagem):
    channel.basic_publish(
        exchange='',
        routing_key='fila_sensor_presenca',
        body=mensagem
    )
    print("Mensagem enviada")

if __name__ == '__main__':
    channel = configurar_sensor_temperatura_rabbitMQ()
    while (True):
        presenca = random.randint(0, 1)

        if (presenca):
            print(f"Presença: {presenca}")
            mandar_mensagem(channel, "S")
        else:
            print(f"Presença: {presenca}")
            mandar_mensagem(channel, "N")
        
        
        time.sleep(5)