import pika
from flask import Flask, jsonify
from concurrent import futures
from datetime import datetime
import threading
import pika
from mensagem_pb2 import Comando
from mensagem_pb2_grpc import ArCondicionadoServiceServicer, add_ArCondicionadoServiceServicer_to_server
from collections import deque

app = Flask(__name__)

mensagens = {
    "temperatura": deque(maxlen=20),
    "fumaca": deque(maxlen=20),
    "presenca": deque(maxlen=20)
}

def temperatura_callback(ch, method, properties, body):
    queue_name = method.routing_key
    mensagem = body.decode('utf-8')
    try:
        mensagem = int(body.decode('utf-8'))
        mensagens["temperatura"].append(f"Temperatura: {int(mensagem)}     Horário: ${str(datetime.now())}")
    except:
        if (queue_name == "fila_sensor_fumaca"):
            mensagens["fumaca"].append(f"Fumaca: {'Tem fumaça' if mensagem == 'S' else 'Nao tem fumaça'}     Horário: ${str(datetime.now())}")
        else:
            mensagens["presenca"].append(f"Presença: {'Tem gente' if mensagem == 'S' else 'Não tem ninguém'}     Horário: ${str(datetime.now())}")

def fumaca_callback(ch, method, properties, body):
    mensagem = body.decode('utf-8')
    mensagens["fumaca"].append(f"Fumaca: {'Tem fumaça' if mensagem == 'S' else 'Nao tem fumaça'}     Horário: ${str(datetime.now())}")

def presenca_callback(ch, method, properties, body):
    mensagem = body.decode('utf-8')
    mensagens["presenca"].append(f"Presença: {'Tem gente' if mensagem == 'S' else 'Não tem ninguém'}     Horário: ${str(datetime.now())}")


@app.route('/temperatura', methods=['GET'])
def obter_mensagens_temperatura():
    return jsonify({'mensagens': [i for i in mensagens["temperatura"]]})

@app.route('/fumaca', methods=['GET'])
def obter_mensagens_fumaca():
    return jsonify({'mensagens': [i for i in mensagens["fumaca"]]})

@app.route('/presenca', methods=['GET'])
def obter_mensagens_presenca():
    return jsonify({'mensagens': [i for i in mensagens["presenca"]]})

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel_rabbitmq = connection.channel()
    channel_rabbitmq.queue_declare(queue='fila_sensor_temperatura')
    channel_rabbitmq.basic_consume(
        queue='fila_sensor_temperatura', 
        on_message_callback=temperatura_callback, 
        auto_ack=True
    )

    channel_rabbitmq.queue_declare(queue='fila_sensor_fumaca')
    channel_rabbitmq.basic_consume(
        queue='fila_sensor_fumaca', 
        on_message_callback=fumaca_callback, 
        auto_ack=True
    )

    channel_rabbitmq.queue_declare(queue='fila_sensor_presenca')
    channel_rabbitmq.basic_consume(
        queue='fila_sensor_presenca', 
        on_message_callback=temperatura_callback, 
        auto_ack=True
    )

    temperatura_thread = threading.Thread(target=channel_rabbitmq.start_consuming)
    temperatura_thread.start()

    app.run(port=5000)
