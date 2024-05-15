# Ler 4 números inteiros e calcular a soma dos que forem par.

num = []

for i in range(4):
    num_ask = (int(input(f'Digite o {i+1}° número: ')))
    print()

    if num_ask % 2 == 0:
        num.append(num_ask)

if num == []:
    print('Nenhum número par foi digitado')
else:
    print(f'A soma dos números pares é {sum(num)}')