def classificar_idade_nadador(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Adulto"

# Exemplo de uso
idade_nadador = int(input("Digite a idade do nadador: "))
classificacao = classificar_idade_nadador(idade_nadador)
print("Classificação:", classificacao)