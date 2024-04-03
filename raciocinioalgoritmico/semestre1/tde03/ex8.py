num = float(input("Digite um número: "))
total = 0
contagem = 1
while contagem < 11:
    total += num
    num = float(input("Digite um número: "))
    contagem += 1
    if contagem == 10:
        media = total / (contagem)
        print("A média dos números digitados é: ", media)
        print("A soma dos números digitados é: ", total)