import random
from tabulate import tabulate

# Definição das cartas
personagens = ["Lógica", "Silogismo", "Premissa", "Sofismo", "Falácia", "Retórica"]
armas = ["Implicação", "Contraposição", "Bi implicação", "Entimema"]
locais = ["Contigência", "Tautologia", "Contradição", "Equivalência"]

# Definição dos dados da tabela e cartas reveladas
personagens_t = ["Lógica", "Silogismo", "Premissa", "Sofismo", "Falácia", "Retórica"]
armas_t = ["Implicação", "Contraposição", "Bi implicação", "Entimema"]
locais_t = ["Contigência", "Tautologia", "Contradição", "Equivalência"]
cartas_reveladas = []  # Lista para armazenar as cartas reveladas durante o jogo


# Solução do mistério (gerada aleatoriamente)
solucao = {
    "personagem": random.choice(personagens),
    "arma": random.choice(armas),
    "local": random.choice(locais)
}

# Remove a carta da solução das cartas disponíveis
personagens.remove(solucao["personagem"])
armas.remove(solucao["arma"])
locais.remove(solucao["local"])

print("Solução:", solucao)

    # Função para exibir a tabela de personagens, armas e locais, ocultando as cartas já reveladas.
def exibir_tabela(personagens_t, armas_t, locais_t, cartas_reveladas):
    # Inicializa uma lista vazia para armazenar os dados da tabela.
    dados = []

    # Determina o comprimento máximo entre as listas de personagens, armas e locais.
    max_len = max(len(personagens_t), len(armas_t), len(locais_t))

    # Itera sobre o intervalo de 0 até o comprimento máximo, criando uma linha para cada iteração.
    for i in range(max_len):
        linha = []  # Inicializa uma lista vazia para armazenar os dados da linha atual.

        # Se o índice atual for menor que o comprimento da lista de personagens, adiciona o personagem à linha
        # se ele não estiver na lista de cartas reveladas. Caso contrário, adiciona uma string vazia.
        if i < len(personagens_t):
            linha.append(personagens_t[i] if personagens_t[i] not in cartas_reveladas else "")
        else:
            linha.append("")

        # Repete o mesmo processo para as listas de armas e locais.
        if i < len(armas_t):
            linha.append(armas_t[i] if armas_t[i] not in cartas_reveladas else "")
        else:
            linha.append("")

        if i < len(locais_t):
            linha.append(locais_t[i] if locais_t[i] not in cartas_reveladas else "")
        else:
            linha.append("")

        # Adiciona a linha completa à lista de dados da tabela.
        dados.append(linha)

    # Define os cabeçalhos das colunas da tabela.
    cabecalho = ["Personagens", "Armas", "Locais"]

    # Imprime a tabela formatada usando a biblioteca 'tabulate'.
    print(tabulate(dados, headers=cabecalho, tablefmt="grid"))

# Distribuição de cartas para os jogadores
def distribuir_cartas(num_jogadores):
    # Cria uma lista com todas as cartas disponíveis
    cartas_disponiveis = personagens + armas + locais
    random.shuffle(cartas_disponiveis)

    # Calcula quantas cartas cada jogador deve receber
    num_cartas_por_jogador = len(cartas_disponiveis) // num_jogadores
    num_cartas_extra = len(cartas_disponiveis) % num_jogadores

    cartas_jogadores = {}
    inicio = 0
    for i in range(num_jogadores):
        fim = inicio + num_cartas_por_jogador + (1 if i < num_cartas_extra else 0)
        cartas_jogadores[f"jogador{i + 1}"] = cartas_disponiveis[inicio:fim]
        inicio = fim

    # Impressão das cartas distribuídas para auditoria
    print("\nCartas distribuídas para cada jogador (apenas auditoria):")
    for jogador, cartas in cartas_jogadores.items():
        print(f"{jogador}: {', '.join(cartas)}")

    return cartas_jogadores

# Verificação da acusação do jogador
def verificar_acusacao(acusacao):
    return acusacao == solucao

# Função para pedir uma pista
def pedir_pista(cartas_jogadores, pistas_jogador):
    if len(pistas_jogador) < 3:
        # Cria uma lista de todas as cartas dos jogadores
        cartas_jogadores_flat = [carta for cartas in cartas_jogadores.values() for carta in cartas]
        # Remove as pistas que já foram dadas
        for pista in pistas_jogador:
            if pista in cartas_jogadores_flat:
                cartas_jogadores_flat.remove(pista)
        # Escolhe uma carta aleatória para ser a pista
        if cartas_jogadores_flat:
            pista = random.choice(cartas_jogadores_flat)
            return pista
        else:
            return "Não há mais pistas disponíveis."
    else:
        return "Você já recebeu o número máximo de pistas."

# Função principal do jogo
def jogar():
    # Mensagem de boas-vindas e solicitação do número de jogadores
    print("Bem-vindos ao jogo 'Assassinaram a Lógica'!")

    # Validação do número de jogadores
    while True:
        num_jogadores = input("Digite o número de jogadores (até 4): ")
        try:
            num_jogadores = int(num_jogadores)
            if 1 <= num_jogadores <= 4:
                break
            else:
                print("Valor inválido.") 
        except ValueError:
            continue
    # Solicitação dos nomes dos jogadores
    jogadores = {}
    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        jogadores[f"jogador{i + 1}"] = nome

    while True:
        num_turnos = input("Digite o número de turnos por jogador (ou '0' para ilimitado): ")
        try:
            num_turnos = int(num_turnos)
            if num_turnos >= 0:
                break
            else:
                print("Valor inválido. Digite um número maior ou igual a zero.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    turnos_restantes = {jogador: num_turnos for jogador in jogadores.keys()}


    # Impressão das cartas distribuídas para auditoria
    print("\nAs cartas foram distribuídas. Que comece a investigação!\n")
    print("Os suspeitos são Silogismo, Premissa, Sofismo, Falácia e Retórica")
    print("As armas do crime são Implicação, Contraposição, Bi implicação, Entimema")
    print("Os locais são Contingência, Tautologia, Contradição, Equivalência")

    cartas_jogadores = distribuir_cartas(num_jogadores)  # Distribui as cartas para os jogadores
    pistas_jogadores = {jogador: [] for jogador in jogadores.keys()}  # Inicializa lista de pistas para cada jogador

    jogador_atual = 1  # Define o jogador inicial

    exibir_tabela(personagens_t, armas_t, locais_t, cartas_reveladas) # Exibe a tabela inicial com todos os dados

    while True:  # Loop principal do jogo
        for _ in range(num_jogadores):  # Para cada jogador
            jogador = f"jogador{jogador_atual}"  # Determina o jogador atual
            print(f"\nÉ a vez de {jogadores[jogador]}. Turnos restantes: {turnos_restantes[jogador]}")

            # Solicita ação ao jogador: pergunta, acusação ou pedido de pista
            acao = input("Você gostaria de fazer uma pergunta sobre personagem (p), arma (a), local (l), fazer uma acusação (k) ou pedir uma pista (t)? ")
            acao = acao.lower()
            while acao not in ['p', 'a', 'l', 'k', 't']:
                acao = input("Inválido. Digite uma opção válida. \n personagem (p), arma (a), local (l), fazer uma acusação (k) ou pedir uma pista (t)? ")

            # Se o jogador escolhe fazer uma pergunta sobre personagem, arma ou local
            if acao in {"p", "a", "l"}:
                categoria = {"p": "personagem", "a": "arma", "l": "local"}[acao]
                if acao == 'p':
                    pergunta = input('Digite o nome do personagem: ').capitalize()
                    while pergunta not in personagens_t:
                        print(pergunta)
                        pergunta = input('Valor inválido, digite o nome do personagem: ').capitalize()
                elif acao == 'a':
                    pergunta = input('Digite o nome da arma: ').capitalize()
                    while pergunta not in armas_t:
                        pergunta = input('Valor inválido, digite o nome da arma: ').capitalize()
                else:
                    pergunta = input('Digite o nome do local: ').capitalize()
                    while pergunta not in locais_t:
                        pergunta = input('Valor iválido, digite o nome do local: ').capitalize()
                if pergunta in cartas_jogadores[jogador]:
                    print("Sim, a carta está em sua mão.")
                    cartas_reveladas.append(pergunta) # Adiciona o item à lista de cartas reveladas
                else:
                    print("Não, a carta não está em sua mão.")

                exibir_tabela(personagens_t, armas_t, locais_t, cartas_reveladas) # Reexibe a tabela atualizada

            # Se o jogador escolhe fazer uma acusação
            elif acao == "k":
                # Solicita as cartas da acusação
                acusacao_personagem = input("Digite o personagem da acusação: ").capitalize()
                acusacao_personagem = acusacao_personagem
                acusacao_local = input("Digite o local da acusação: ").capitalize()
                acusacao_local = acusacao_local
                acusacao_arma = input("Digite a arma da acusação: ").capitalize()
                acusacao_arma = acusacao_arma
                # Verifica se a acusação está correta e informa o resultado
                acusacao_jogador = {
                    "personagem": acusacao_personagem,
                    "local": acusacao_local,
                    "arma": acusacao_arma
                }
                if verificar_acusacao(acusacao_jogador):
                    print("Parabéns! Você descobriu a verdade.")
                    return  # Encerra o jogo
                else:
                    print("Infelizmente, sua acusação está incorreta. Você está eliminado do jogo.")
                    return  # Encerra o jogo

            # Se o jogador escolhe pedir uma pista
            elif acao == "t":
                pista = pedir_pista(cartas_jogadores, pistas_jogadores[jogador])  # Solicita uma pista
                print(f"{jogadores[jogador]}, sua pista é: {pista}")  # Imprime a pista
                pistas_jogadores[jogador].append(pista)  # Adiciona a pista à lista de pistas do jogador

            turnos_restantes[jogador] -= 1

            if turnos_restantes[jogador] == 0:
                print(f"{jogadores[jogador]} está sem turnos e foi eliminado!")
                del jogadores[jogador]  # Remove o jogador do jogo
                num_jogadores -= 1
                if num_jogadores == 1:
                    jogador_vencedor = list(jogadores.keys())[0]
                    print(f"\n{jogadores[jogador_vencedor]} venceu o jogo!")
                    return

            # Passa para o próximo jogador
            jogador_atual = jogador_atual % num_jogadores + 1

        # Se todos os jogadores fizeram suas perguntas, inverte a ordem para a próxima rodada
        jogador_atual = num_jogadores

if __name__ == "__main__":
    jogar()