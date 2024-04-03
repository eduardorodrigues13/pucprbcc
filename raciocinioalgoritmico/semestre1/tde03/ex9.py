lI = int(input("Digite um limite inicial: "))
lF = int(input("Digite um limite final: "))

num = lI
while num < lF:
    if num % 3 == 0:
        print(num)
    num += 1