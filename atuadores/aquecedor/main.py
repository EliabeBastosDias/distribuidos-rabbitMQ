import grpc
from concurrent import futures
import time

from mensagem_pb2 import Comando
from mensagem_pb2_grpc import AquecedorServiceServicer, add_AquecedorServiceServicer_to_server

class Aquecedor(AquecedorServiceServicer):
    def _init_(self):
        self.ligado = False

    def EnviarComando(self, request, context):
        if request.comando == 'S':
            self.ligado = True
            print("Aquecedor ligado.")
        elif request.comando == 'N':
            self.ligado = False
            print("Aquecedor desligado.")
        else:
            print("Comando desconhecido.")
        return Comando(comando=request.comando)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AquecedorServiceServicer_to_server(Aquecedor(), server)
    server.add_insecure_port('[::]:50059')
    server.start()
    print("Servidor gRPC iniciado na porta 50059")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()