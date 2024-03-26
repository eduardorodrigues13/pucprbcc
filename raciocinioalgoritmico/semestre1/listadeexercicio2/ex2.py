import datetime

def calcular_idade(mes_nascimento, ano_nascimento):
    ano_atual = datetime.datetime.now().year
    mes_atual = datetime.datetime.now().month

    idade = ano_atual - ano_nascimento

    if mes_atual < mes_nascimento:
        idade -= 1

    return idade

def verificar_elegibilidade_cnh(idade):
    if idade >= 18:
        return "Você está elegível para solicitar uma carteira de motorista."
    else:
        return "Você ainda não está elegível para solicitar uma carteira de motorista."

def main():
    mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
    ano_nascimento = int(input("Digite o ano de nascimento: "))

    idade = calcular_idade(mes_nascimento, ano_nascimento)
    print("Em 2024, você terá", idade, "anos.")
    print(verificar_elegibilidade_cnh(idade))

if __name__ == "__main__":
    main()
