# A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto fornecido.

num = []

for i in range(10):
    num.append(int(input(f'Digite o {i+1}° número: ')))

print(f'O valor máximo é {max(num)}')
print(f'O valor mínimo é {min(num)}')
print(f'A amplitude amostral é {max(num) - min(num)}')