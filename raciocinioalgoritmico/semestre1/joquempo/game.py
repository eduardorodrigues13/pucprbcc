import random

# Imprime a mensagem de boas-vindas ao jogo
print("BEM-VINDO AO JOKENPÔ!")

# Solicita ao jogador que escolha o modo de jogo
modoJogo = int(input("PARA INICIAR, ENTRE UMA OPÇÃO: \n (1) 2 PLAYERS \n (2) PLAYER VS COMP \n (3) COMP x COMP \n"))

# Verifica se o modo de jogo escolhido é válido
if modoJogo in [1, 2, 3]:
    # Modo de jogo 2 players
    if modoJogo == 1:
        print("MODO 2 PLAYERS")
        # Solicita aos jogadores que informem seus nomes
        j1Name = input("QUAL O SEU NOME P1? ")
        j2Name = input("QUAL O SEU NOME P2? ")
    # Modo de jogo player vs comp
    elif modoJogo == 2:
        print("MODO PLAYER VS COMP")
        # Solicita ao jogador que informe seu nome
        j1Name = input("QUAL O SEU NOME PLAYER? ")
        # Define o nome do jogador 2 como "COMPUTADOR"
        j2Name = "COMPUTADOR"
    # Modo de jogo comp vs comp
    else:
        print("COMP VS COMP")
        # Define o nome do jogador 1 como "COMPUTADOR 1"
        j1Name = "COMPUTADOR 1"
        # Define o nome do jogador 2 como "COMPUTADOR 2"
        j2Name = "COMPUTADOR 2"

    # Inicializa os pontos dos jogadores
    j1Pontos = 0
    j2Pontos = 0
    opcao = 1

    # Loop principal do jogo
    while opcao == 1:
        # Exibe as opções de jogada
        print("OPÇÕES:\n (1) PEDRA \n (2) PAPEL \n (3) TESOURA \n")
        # Solicita a jogada do jogador 1
        jogadorUm = int(input("{}, ENTRE A SUA JOGADA: ".format(j1Name))) if modoJogo != 3 else random.randint(1, 3)
        # Solicita a jogada do jogador 2
        jogadorDois = int(input("{}, ENTRE A SUA JOGADA: ".format(j2Name))) if modoJogo == 1 else random.randint(1, 3)

        print("-----------------------------------")
        # Verifica se a jogada do jogador 1 é válida
        while jogadorUm not in [1, 2, 3]:
            jogadorUm = int(input("JOGADA INVÁLIDA! É PEDRA, PAPEL OU TESOURA! \n DIGITE A JOGADA: "))
        # Verifica se a jogada do jogador 2 é válida
        while jogadorDois not in [1, 2, 3]:
            jogadorDois = int(input("JOGADA INVÁLIDA! É PEDRA, PAPEL OU TESOURA! \n DIGITE A JOGADA: "))

        # Exibe a jogada do jogador 1
        if jogadorUm == 1:
            print("{} JOGOU PEDRA".format(j1Name))
            print("-----------------------------------")
        elif jogadorUm == 2:
            print("{} JOGOU PAPEL".format(j1Name))
            print("-----------------------------------")
        elif jogadorUm == 3:
            print("{} JOGOU TESOURA".format(j1Name))
            print("-----------------------------------")

        # Exibe a jogada do jogador 2
        if jogadorDois == 1:
            print("{} JOGOU PEDRA".format(j2Name))
            print("-----------------------------------")
        elif jogadorDois == 2:
            print("{} JOGOU PAPEL".format(j2Name))
            print("-----------------------------------")
        elif jogadorDois == 3:
            print("{} JOGOU TESOURA".format(j2Name))
            print("-----------------------------------")

        # Verifica o resultado da partida
        if jogadorUm == jogadorDois:
            print("EMPATE!\n")
        elif (jogadorUm == 1 and jogadorDois == 2) or (jogadorUm == 2 and jogadorDois == 3) or (
                jogadorUm == 3 and jogadorDois == 1):
            print("VITÓRIA DE {}!".format(j2Name))
            j2Pontos += 1
        else:
            print("VITÓRIA DE {}!".format(j1Name))
            j1Pontos += 1

        print("-----------------------------------")
        # Exibe o placar atual
        print("PLACAR: {} [{} X {}] {}".format(j1Name, j1Pontos, j2Pontos, j2Name))
        # Solicita ao jogador se deseja continuar jogando
        opcao = 0
        while opcao not in [1, 2]:
            opcao = int(input("CONTINUAR? \n (1) SIM \n (2) ENCERRAR "))

    print("-----------------------------------")
    # Exibe o placar final
    print("PLACAR: {} [{} X {}] {}".format(j1Name, j1Pontos, j2Pontos, j2Name))
    print("FIM DE JOGO! AT.TE, EDUARDO RODRIGUES.")
else:
    print("OPÇÃO INVÁLIDA!")