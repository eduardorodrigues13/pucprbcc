#Exercício 3
lista = [0]*10
i = 0
while i < len(lista):
    lista[i] = int(input(f'Insira um valor para o indice {i} de 10: '))
    i += 1
print(lista)
atualizar_lista = 0
atualizar_lista = int(input('Deseja atualizar a sua lista?\n 1 - SIM\n 2- NÃO'))

while atualizar_lista == 1:
    n = int(input('Insira o valor: '))
    index = int(input('Insira o valor do indíce: '))
    lista.pop(index)
    lista.insert(index, n)
    atualizar_lista = int(input('Deseja atualizar a sua lista?\n 1 - SIM\n 2- NÃO'))
    print(lista)
