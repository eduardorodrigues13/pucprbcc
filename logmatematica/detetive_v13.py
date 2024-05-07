import random

# Definição das cartas
personagens = ["Lógica", "Silogismo", "Premissa", "Sofismo", "Falácia", "Retórica"]
armas = ["Implicação", "Contraposição", "Bi implicação", "Entimema"]
locais = ["Contingencia", "Tautologia", "Contradição", "Equivalência"]

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
    num_jogadores = int(input("Digite o número de jogadores (até 4): "))
    # Validação do número de jogadores
    while num_jogadores < 2 or num_jogadores > 4:
        print("Número inválido de jogadores. Por favor, escolha entre 2 e 4 jogadores.")
        num_jogadores = int(input("Digite o número de jogadores (até 4): "))

    # Solicitação dos nomes dos jogadores
    jogadores = {}
    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        jogadores[f"jogador{i + 1}"] = nome

    # Impressão das cartas distribuídas para auditoria
    print("\nAs cartas foram distribuídas. Que comece a investigação!\n")
    print("Os suspeitos são Silogismo, Premissa, Sofismo, Falácia e Retórica")
    print("As armas do crime são Implicação, Contraposição, Bi implicação, Entimema")
    print("Os locais são Contingencia, Tautologia, Contradição, Equivalência")

    cartas_jogadores = distribuir_cartas(num_jogadores)  # Distribui as cartas para os jogadores
    pistas_jogadores = {jogador: [] for jogador in jogadores.keys()}  # Inicializa lista de pistas para cada jogador

    jogador_atual = 1  # Define o jogador inicial

    while True:  # Loop principal do jogo
        for _ in range(num_jogadores):  # Para cada jogador
            jogador = f"jogador{jogador_atual}"  # Determina o jogador atual
            print(f"\nÉ a vez de {jogadores[jogador]}.")

            # Solicita ação ao jogador: pergunta, acusação ou pedido de pista
            acao = input(
                "Você gostaria de fazer uma pergunta sobre personagem (p), arma (a), local (l), fazer uma acusação (k) ou pedir uma pista (t)? ")

            # Se o jogador escolhe fazer uma pergunta sobre personagem, arma ou local
            if acao in {"p", "a", "l"}:
                categoria = {"p": "personagem", "a": "arma", "l": "local"}[acao]
                pergunta = input(f"Qual {categoria} você gostaria de perguntar? ")  # Solicita a pergunta
                # Verifica se a carta está na mão do jogador e informa o resultado
                if pergunta in cartas_jogadores[jogador]:
                    print("Sim, a carta está em sua mão.")
                else:
                    print("Não, a carta não está em sua mão.")

            # Se o jogador escolhe fazer uma acusação
            elif acao == "k":
                # Solicita as cartas da acusação
                acusacao_personagem = input("Digite o personagem da acusação: ")
                acusacao_local = input("Digite o local da acusação: ")
                acusacao_arma = input("Digite a arma da acusação: ")
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

            # Passa para o próximo jogador
            jogador_atual = jogador_atual % num_jogadores + 1

        # Se todos os jogadores fizeram suas perguntas, inverte a ordem para a próxima rodada
        jogador_atual = num_jogadores

if __name__ == "__main__":
    jogar()
