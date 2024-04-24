import random

numeros_aleatorios = [0]*6
numeros_apostados = [0]*6
acertos = 0

i = 0
while i < len(numeros_aleatorios):
    numeros_aleatorios[i] = random.randint(1,60)
    i += 1

i = 0
while i < len(numeros_aleatorios):
    numeros_apostados[i] = int(input(f'Digite o número de posição {i + 1}: '))
    if numeros_apostados[i] > 60 or numeros_apostados[i] < 1:
        numeros_apostados[i] = int(input('Valor inválido, tente novamente.'))
    i += 1

i = 0
while i < len(numeros_aleatorios):
    print(f'NÚMERO SORTEADO - {numeros_aleatorios[i]} | {numeros_apostados[i]} - SEU NÚMERO')
    if numeros_apostados[i] in numeros_aleatorios:
        acertos += 1
    i += 1

print(f'NÚMERO DE ACERTOS: {acertos}')
