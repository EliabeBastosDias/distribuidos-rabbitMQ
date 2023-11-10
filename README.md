# Trabalho Distribuidos - Parte 2

Especificação de sensores e atuadores integrados na simulação de ambiente inteligente de uma casa.
- Sensores: coletam dados do ambiente
- Atuadores: podem agir no ambiente para modificá-lo de alguma forma).

## Sensores
### Temperatura (range)
Informa a temperatura atual.
==> ativa/desliga atuador Ar Condicionado
==> ativa/desliga atuador Aquecedor

### Fumaça (up/down)
Informa se há detecção de Fumaça.
==> ativa atuador Sprinklers

### Luminosidade (range)
==> ativa/desliga atuador Luz Externa
==> ativa/desliga sensor de Presença

### Presença (up/down)
Informa se há movimentação na área próxima.
==> ativa/desliga atuador Luz Externa

## Atuadores
### Ar Condicionado
==> Liga/Desliga
==> Configura Temperatura Desejada (apenas se ligado)

### Aquecedor
==> Liga/Desliga
==> Configura Temperatura Desejada (apenas se ligado)

### Sprinkler
==> Liga/Desliga

### Luz Externa
==> Liga/Desliga
