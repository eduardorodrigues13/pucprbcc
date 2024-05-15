import random
qtdLinhas = 4
qtdColunas = 4
matriz = []

lista = []

for i in range(qtdLinhas):
    vetor = []
    for j in range(qtdColunas):
        vetor.append(random.randint(1, 100))
    matriz.append(vetor)


for linha in matriz:
    print(linha)

for linha in matriz:
    for item in linha:
        lista.append(item)
print(sum(lista))
