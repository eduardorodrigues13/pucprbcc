# Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

num = []

for i in range(3):
    num.append(int(input(f'Digite o {i+1}° número: ')))

if num[0] > num[1] + num[2]:
    print(f'{num[0]} é maior que a soma de {num[1]} e {num[2]}')
else:
    print(f'{num[0]} não é maior que a soma de {num[1]} e {num[2]}')