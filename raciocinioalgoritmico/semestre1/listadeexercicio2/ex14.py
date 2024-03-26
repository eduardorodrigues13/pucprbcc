# Leia três números inteiros do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Crie uma lista com os três números
numeros = [num1, num2, num3]

# Ordene a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprima os números em ordem decrescente
print("Números em ordem decrescente:", numeros)