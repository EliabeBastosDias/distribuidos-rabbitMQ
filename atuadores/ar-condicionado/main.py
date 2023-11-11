# ar_condicionado_server.py

import grpc
from concurrent import futures
import time

from ar_condicionado_pb2 import Comando
from ar_condicionado_pb2_grpc import ArCondicionadoServiceServicer, add_ArCondicionadoServiceServicer_to_server

class ArCondicionado(ArCondicionadoServiceServicer):
    def __init__(self):
        self.ligado = False

    def EnviarComando(self, request, context):
        if request.comando == 'S':
            self.ligado = True
            print("Ar condicionado ligado.")
        elif request.comando == 'N':
            self.ligado = False
            print("Ar condicionado desligado.")
        else:
            print("Comando desconhecido.")
        return Comando(comando=request.comando)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ArCondicionadoServiceServicer_to_server(ArCondicionado(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Servidor gRPC iniciado na porta 50052")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
