num = float(input("Digite um número: "))
total = 0
contagem = 0
while num != -1:
    total += num
    num = float(input("Digite um número: "))
    contagem += 1
    if num == -1:
        media = total / (contagem)
        print("A média dos números digitados é: ", media)
print("Valor de saída: -1. Encerrando...")