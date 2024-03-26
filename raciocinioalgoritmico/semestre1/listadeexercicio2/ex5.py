num_copias = int(input("Digite o número de cópias: "))

if num_copias < 100:
    custo = num_copias * 0.25
else:
    custo = num_copias * 0.20

print("Custo total: R$", custo)