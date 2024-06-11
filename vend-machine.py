from tabulate import tabulate

# Importando a biblioteca tabulate para formatar a tabela

# Função para imprimir a tabela de produtos
def imprimir():
    headers = ["ID", "Produto", "Preço", "Quantidade"]
    print(tabulate(maquina, headers=headers, tablefmt="grid"))

# Função para calcular o troco
def calculadora_troco(codigo):
    # Obtendo o valor do produto com base no código
    valor_produto = maquina[codigo - 1][2]
    print(f'Valor a pagar: R${valor_produto:.2f}')
    valor_pago = input("Digite o valor de pagamento: R$")

    # Verificando se o valor pago é válido
    while not valor_pago.replace('.', '', 1).isdigit() or float(valor_pago) < valor_produto:
        valor_pago = input("Digite o valor de pagamento: R$")

    valor_pago = float(valor_pago)
    troco = valor_pago - valor_produto

    # Definindo as notas disponíveis e a quantidade em estoque
    notas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    estoque_notas = {
        200: 5, 100: 10, 50: 10, 20: 10, 10: 20, 5: 20, 2: 50,
        1: 100, 0.50: 100, 0.25: 100, 0.10: 100, 0.05: 100, 0.01: 100
    }

    # Calculando as notas do troco
    notas_troco = {}
    for nota in notas:
        if troco >= nota:
            quantidade = int(troco // nota)
            if estoque_notas[nota] < quantidade:
                quantidade = estoque_notas[nota]
            troco = round(troco - quantidade * nota, 2)
            estoque_notas[nota] -= quantidade
            notas_troco[nota] = quantidade

    print(f'Troco restante: R${troco:.2f}')

    # Mostrando as notas do troco
    if notas_troco:
        print("Notas do troco:")
        for nota, quantidade in notas_troco.items():
            print(f'{quantidade} nota(s) de R${nota:.2f}')

    # Verificando se a compra foi realizada com sucesso
    if troco > 0.01:
        print(f'Compra não realizada. Devolvendo R${valor_pago:.2f} ao cliente.')
        return False
    elif troco == 0.01:
        estoque_notas[0.01] -= 1
        troco = 0
        print(f'Compra realizada com sucesso.')
    else:
        print(f'Compra realizada com sucesso. Troco: R${troco:.2f}')
        return True

# Função para perguntar se o usuário deseja fazer algo novamente
def novamente(acao):
    while True:
        try:
            continuar = int(input(f'Deseja fazer {acao} novamente? (1-Sim, 0-Não): '))
            if continuar in [0, 1]:
                return continuar
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Função para cadastrar um novo produto
def cadastro():
    continuar = 1
    while continuar == 1:
        vetor = []
        vetor.append(int(len(maquina)+1))
        vetor.append(input("Digite o nome do produto: "))
        vetor.append(float(input("Digite o valor do produto:")))
        vetor.append(int(input("Digite a quantidade do estoque do produto:")))
        maquina.append(vetor)
        imprimir ()
        continuar = novamente("Novo cadastro")

# Função para editar um produto existente
def editar():
    continuar = 1 
    imprimir()
    while continuar == 1:
        limite_de_edicao = len(maquina[0])
        editar = 1
        while editar == 1:
            edicao = int(input("Digite o codigo do produto:"))
            imprimir()
            if 1 <= edicao <= limite_de_edicao:
                edicao_do_produto = 0
                while edicao_do_produto not in [1,2,3]:
                    print()
                    print("1 - Alterar o nome do produto")
                    print("2 - Alterar o valor do produto")
                    print("3 - Alterar a quantidade do estoque")
                    edicao_do_produto = int(input("Escolha uma das opções: "))
                    if edicao_do_produto == 1:
                        nome = input("Digite o nome do produto: ")
                        maquina[edicao - 1][1] = nome
                    elif edicao_do_produto == 2:
                        valor = float(input("Digite o novo valor do produto: "))
                        maquina[edicao - 1][2] = valor
                    elif edicao_do_produto == 3:
                        estoque = int(input("Digite o a quantidade que tem no estoque: "))
                        maquina[edicao - 1][3] = estoque
                    else :
                        print("Opção inválida. Tente novamente.")

                    imprimir()
                    editar = novamente("noava edição dos produtos ")
                    if editar == 1:
                        edicao_do_produto = 0

                    editar = 0
            else:
                print("Este codigo não existe. Tente novamente.")
        continuar = novamente("edição")

# Função para remover um produto existente
def remover():
    continuar = 1
    while continuar == 1:
        editar = 1
        imprimir()
        while editar == 1:
            limite_de_remocao = len(maquina)
            remover = int(input("Digite o código que queira remover: "))
            if 1 <= remover <= limite_de_remocao:
                maquina.pop(remover - 1) 
                for i in range(remover - 1, limite_de_remocao - 1):
                    maquina[i][0] -= 1
                imprimir()
                editar = 0
            else:
                print("Código inválido. Tente novamente.")
        continuar = novamente("remover")

# Função para realizar uma venda
def venda():
    while True:
        try:
            codigo = int(input("Escolha uma das opções acima: "))
            if 1 <= codigo <= len(maquina):
                return codigo
            elif codigo == 1989:
                return codigo
            else:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Função para verificar se há estoque suficiente do produto
def estoque(codigo):
    if maquina[codigo - 1][3] == 0:
        print('Produto indisponível.')
        return False
    else:
        maquina[codigo - 1][3] -= 1
        return True

# Função para entrar no modo administrador
def modoAdm():
    print("1 - Cadastro de produto")
    print("2 - Edição de produto")
    print("3 - Remoção de produto")
    print("4 - Sair do modo administrador")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        return
    else:
        print("Opção inválida. Tente novamente.")

# Lista de produtos na máquina
maquina = [
    [1, "Coca-Cola", 3.75, 2], 
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1], 
    [4, "Café", 1.25, 100],
    [5, "RedBull", 13.99, 2]
]

# Loop principal para executar a máquina
while True:
    imprimir()
    codigo = venda()
    if codigo == 1989:
        modoAdm()
    else:
        if estoque(codigo):
            if calculadora_troco(codigo):
                continuar = novamente("outra compra")
                if continuar == 0:
                    break
            else:
                continuar = novamente("a compra")
                if continuar == 0:
                    break
        else:
            continuar = novamente("a compra")
            if continuar == 0:
                break
