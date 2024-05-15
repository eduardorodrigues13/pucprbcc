# Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is) posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.

num = []

for i in range(10):
    num.append(int(input(f'Digite o {i+1}° número: ')))

search = int(input('Digite um número para pesquisar no vetor: '))

if search in num:
    print(f'O número {search} foi encontrado {num.count(search)} vezes na(s) posição(ões): ')

    for i in range(len(num)):
        if num[i] == search:
            print(f'{i+1}')
else:
    print(f'O número {search} não foi encontrado no vetor')