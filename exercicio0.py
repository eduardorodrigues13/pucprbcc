notaProva1 = float(input("Digite a nota de sua primeira prova: "))
notaProva2 = float(input("Digite a nota de sua segunda prova: "))
mediaProva = (notaProva1 + notaProva2) / 2
porcentagemFreq = float(input("Digite a sua frequência:"))

if mediaProva >= 7 and porcentagemFreq >= 75:
    print("Você está aprovado.")
elif mediaProva >= 4 and porcentagemFreq >= 75:
    print("Você está em recuperação.")
else:
    print("Você está reprovado.")



