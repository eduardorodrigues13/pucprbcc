# Solicitar ao usuário que digite um valor para N
N = float(input("Digite um valor para N: "))
if N % 1 != 0:
    print("O valor digitado não é um número inteiro.")
    exit()
else:
    # Calcular a soma dos primeiros N inteiros, é uma P.A. de razão 1
    soma = (N * (N + 2)) // 2

    # Imprimir a soma
    print("A soma dos primeiros", N, "inteiros é:", soma)
