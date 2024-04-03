numero = 1

while numero <= 10:
    multiplicador = 1
    while multiplicador <= 10:
        resultado = numero * multiplicador 
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1
    print()
    numero += 1
