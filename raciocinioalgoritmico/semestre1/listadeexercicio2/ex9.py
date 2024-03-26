def verificar_classe_eleitoral(idade):
    if idade < 16:
        return "Não votante"
    elif idade >= 18 and idade <= 65:
        return "Eleitor obrigatório"
    else:
        return "Eleitor facultativo"

# Exemplo de uso
idade = int(input("Informe a idade: "))
classe_eleitoral = verificar_classe_eleitoral(idade)
print("Classe eleitoral:", classe_eleitoral)