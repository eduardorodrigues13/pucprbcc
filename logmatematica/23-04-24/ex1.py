# Exercício 1
numeros = [0]*10
i = 0
while i < len(numeros):
    numeros[i] = int(input('Insira um número: '))
    i += 1
i = 0
while i < len(numeros):
    print(f'index: {i}, valor: {numeros[i]}')
    i += 1
