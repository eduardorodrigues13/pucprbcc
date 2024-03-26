def calcular_valor(opcao, preco):
    if opcao == 1:  # À vista
        valor_final = preco - (preco * 0.08)
    elif opcao == 2:  # Em 2 parcelas
        valor_final = preco - (preco * 0.04)
    elif opcao == 3:  # Em 3 parcelas
        valor_final = preco
    elif opcao == 4:  # Em 4 parcelas
        valor_final = preco + (preco * 0.04)
    else:
        print("Opção inválida!")
        return

    print(f"Valor final: R${valor_final:.2f}")


opcao = int(input("Digite a opção desejada (1 - À vista, 2 - Em 2 parcelas, 3 - Em 3 parcelas, 4 - Em 4 parcelas): "))
preco = float(input("Digite o preço de tabela do produto: "))

calcular_valor(opcao, preco)