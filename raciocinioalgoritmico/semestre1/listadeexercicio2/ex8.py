# Ler o número de minutos utilizados no estacionamento
minutos = int(input("Digite o número de minutos utilizados no estacionamento: "))

# Calcular o custo total
if minutos <= 60:
    custo = 8.00
else:
    minutos_extras = minutos - 60
    horas_extras = minutos_extras // 15
    custo = 8.00 + (horas_extras * 1.50)

# Exibir o resultado
if custo == 8.00:
    print("Valor mínimo, R$ 8,00")
else:
    print("Valor fracionado, R$", custo)