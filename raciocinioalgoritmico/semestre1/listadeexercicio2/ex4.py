import math

# Ler o número de entrada
num = int(input("Digite um número: "))

# Verificar se o número é negativo
if num < 0:
    print("Valor inválido")
else:
    # Calcular a raiz quadrada
    sqrt = math.sqrt(num)
    print("Raiz quadrada:", sqrt)
