# Trabalho Distribuidos - Parte 2

--RESUMO:
O trabalho consiste em simular um ambiente inteligente de casa ou escritório. Neste ambiente deverão estar presentes Sensores (que coletam dados do ambiente) e Atuadores (que podem agir no ambiente para modificá-lo de alguma forma).

Todos esses sensores e atuadores serão gerenciados por um servidor chamado Home Assistant. Este equipamento deverá interagir com os sensores e os atuadores coletando informações e, eventualmente, agindo sobre o ambiente.

A comunicação entre os sensores e o Home Assistant ocorrerá via Kafka, usando o paradigma Publisher/Subscriber, onde o Home Assistant se comportará como
Subscriber e cada sensor como Publisher. O sensor deverá publicar periodicamente os dados por ele observados em uma fila/tópico próprio no Kafka, que se encarregará de notificar o Home Assistant sobre a nova mensagem.

A comunicação entre o Home Assistant e os atuadores, por sua vez, deverá ocorrerá via gRPC, usando o paradigma Client/Server, onde o Home Assistent se comportará como Client e cada atuador como Server.

O Home Assistant também deverá se comportar como um servidor para uma aplicação cliente que deve possibilitar interações do usuário com o ambiente inteligente. Através desta aplicação, o usuário poderá receber as informações de momento do ambiente (por exemplo, o nível de luminosidade detectado por cada sensor) e também poderá agir sobre ele (por exemplo, ligando ou desligando uma lâmpada).

## Sensores
### Temperatura (range)
Informa a temperatura atual.
- ativa/desliga atuador Ar Condicionado
- ativa/desliga atuador Aquecedor

### Fumaça (up/down)
Informa se há detecção de Fumaça.
- ativa atuador Sprinklers

### Luminosidade (range)
- ativa/desliga atuador Luz Externa
- ativa/desliga sensor de Presença

### Presença (up/down)
Informa se há movimentação na área próxima.
- ativa/desliga atuador Luz Externa

## Atuadores
### Ar Condicionado
- Liga/Desliga
- Configura Temperatura Desejada (apenas se ligado)

### Aquecedor
- Liga/Desliga
- Configura Temperatura Desejada (apenas se ligado)

### Sprinkler
- Liga/Desliga

### Luz Externa
- Liga/Desliga

## Para manipular um env no python, basta:
- (criar) python3 -m venv myenv
- (ativar) source myenv/bin/activate
- (desativar) deactivate

## Para configurar o rabbitMQ:
- sudo apt-get update
  sudo apt-get install rabbitmq-server
- sudo service rabbitmq-server start
- pip install pika grpcio grpcio-tools protobuf

## Para compilar o .proto:
- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mensagem.proto
