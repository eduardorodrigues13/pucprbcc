# Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
    print()