# Leia dois valores reais do teclado, calcular e imprimir na tela:
# a) A soma destes valores b) O produto deles c) O quociente entre eles

num = []

for i in range(2):
    num.append(float(input(f'Digite o {i+1}° número: ')))

print(f'A soma de {num[0]} e {num[1]} é {num[0] + num[1]}')
print(f'A multiplicação de {num[0]} e {num[1]} é {num[0] * num[1]}')
print(f'O quociente entre {num[0]} e {num[1]} é {num[0] / num[1]}')