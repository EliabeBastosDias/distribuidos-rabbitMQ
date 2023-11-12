# ar_condicionado_server.py

import grpc
from concurrent import futures
import time

from mensagem_pb2 import Comando
from mensagem_pb2_grpc import LampadaServiceServicer, add_LampadaServiceServicer_to_server

class Lampada(LampadaServiceServicer):
    def __init__(self):
        self.ligado = False

    def EnviarComando(self, request, context):
        if request.comando == 'S':
            self.ligado = True
            print("Luz ligada.")
        elif request.comando == 'N':
            self.ligado = False
            print("Luz desligada.")
        else:
            print("Comando desconhecido.")
        return Comando(comando=request.comando)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LampadaServiceServicer_to_server(Lampada(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Servidor gRPC iniciado na porta 50053")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
