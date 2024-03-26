def categorize_boxer(mass):
    mass_lb = mass * 2.20462262

    if mass_lb >= 201:
        return "Peso-pesado"
    elif mass_lb >= 176 and mass_lb <= 200:
        return "Cruzador"
    elif mass_lb >= 169 and mass_lb <= 175:
        return "Meio pesado"
    elif mass_lb >= 161 and mass_lb <= 168:
        return "Super-médio"
    else:
        return "Categoria inferior a Super-médio"

# Example usage
boxer_mass = float(input("Digite a massa do boxeador em kg: "))
category = categorize_boxer(boxer_mass)
print(f"O boxeador pertence à categoria: {category}")