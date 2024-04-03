moeda = int(input("Digite uma opção: 1 - Dolar, 2 - Euro, 3 - Libra: "))
if moeda == 1:
    montante = float(input("Digite o montante em dólares: "))
    cotacao = 5.40
    conversao = montante * cotacao
    if conversao < 1000:
        total = conversao + (conversao * 0.05)
        print(total)
    else:
        total = conversao + (conversao * 0.03)
        print(total)
elif moeda == 2:
    montante = float(input("Digite o montante em euros: "))
    cotacao = 6.57
    conversao = montante * cotacao
    if conversao < 1000:
        total = conversao + (conversao * 0.05)
        print(total)
    else:
        total = conversao + (conversao * 0.03)
        print(total)
elif moeda == 3:
    montante = float(input("Digite o montante em libras: "))
    cotacao = 7.18
    conversao = montante * cotacao
    if conversao < 1000:
        total = conversao + (conversao * 0.05)
        print(total)
    else:
        total = conversao + (conversao * 0.03)
        print(total)