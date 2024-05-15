import random

matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(1, 100)

for linha in matriz:
    print(linha)

for i in range(4):
    for j in range(4):
        if i == j:
            print(matriz[i][j])