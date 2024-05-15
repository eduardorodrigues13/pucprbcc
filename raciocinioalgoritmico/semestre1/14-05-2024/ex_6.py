# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é
# triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.

num = int(input('Digite um número: '))

i = 1

while (i * (i+1) * (i+2)) < num:
    i += 1

if i * (i+1) * (i+2) == num:
    print("É triangular")
else:
    print("Não é triangular")
        