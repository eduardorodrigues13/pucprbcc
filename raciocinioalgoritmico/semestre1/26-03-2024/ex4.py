contNum = 0
pares = 0
impares = 0
while contNum < 10:
    num = float(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contNum += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
    