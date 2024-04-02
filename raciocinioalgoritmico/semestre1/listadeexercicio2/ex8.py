minutos = int(input("Digite a quantidade de minutos: "))
custo = 8.00
tempo_min = 60

if minutos > tempo_min:
    tempo_extra = minutos - tempo_min
    fracao = tempo_extra // 15

    if tempo_extra % 15 != 0:
        fracao += 1

    custo += fracao * 1.50
    print(f"O custo fracionado é de R${custo:.2f}")
else:
    print(f"O custo é de R${custo:.2f}")
    