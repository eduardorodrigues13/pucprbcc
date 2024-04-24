#Exercício 2
vogais = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
texto = input("Insira um texto: ")
i = 0
soma = 0
while i < len(texto):
    if texto[i] in vogais:
        soma += 1
    i += 1
print(soma)
