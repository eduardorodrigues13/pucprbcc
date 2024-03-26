def calcular_peso_ideal(altura, sexo):
    if sexo == 1:  # Masculino
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 2:  # Feminino
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido. Use 1 para masculino e 2 para feminino.")
        return None
    
    return peso_ideal

altura = float(input("Digite a altura em metros: "))
sexo = int(input("Digite o sexo (1 - masculino, 2 - feminino): "))

peso_ideal = calcular_peso_ideal(altura, sexo)
if peso_ideal is not None:
    print("O peso ideal é:", peso_ideal)