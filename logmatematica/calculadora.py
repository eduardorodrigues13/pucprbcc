import re
from tabulate import tabulate

# Função para validar a sintaxe da fórmula proposicional
def validar_formula(formula):
    # Expressão regular para verificar se a fórmula contém apenas caracteres válidos
    padrao = r'^[pqr~^v\->=() ]+$'
    if not re.match(padrao, formula):
        return False
    # Verificando o balanceamento dos parênteses na fórmula
    pilha = []
    for char in formula:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha or pilha.pop() != '(':
                return False
    if pilha:
        return False
    return True

# Função para gerar a tabela verdade com todas as combinações de valores booleanos para as variáveis
def gerar_tabela_verdade(variaveis):
    num_variaveis = len(variaveis)
    num_linhas = 2 ** num_variaveis
    tabela = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_variaveis):
            # Gera os valores de cada variável para cada linha da tabela
            valor = (i >> (num_variaveis - j - 1)) & 1
            linha.append(valor)
        tabela.append(linha)

    return tabela

# Função para avaliar a fórmula proposicional com os valores de variáveis fornecidos
def avaliar_formula(formula, variaveis, valores):
    # Substitui as variáveis pelos seus valores correspondentes na fórmula
    formula_avaliada = formula
    for var, val in zip(variaveis, valores):
        formula_avaliada = re.sub(fr'\b{var}\b', str(val), formula_avaliada)

    # Converte a fórmula para um formato utilizável pelo eval
    formula_avaliada = formula_avaliada.replace('~', ' not ')
    formula_avaliada = formula_avaliada.replace('^', ' and ')
    formula_avaliada = formula_avaliada.replace('v', ' or ')
    formula_avaliada = formula_avaliada.replace('->', ' or not ')
    formula_avaliada = formula_avaliada.replace('=', ' == ')

    # Adiciona parênteses para garantir a precedência correta das operações
    formula_avaliada = re.sub(r'(\d+ or not \d+)', r'(\1)', formula_avaliada)

    # Avalia a expressão usando eval
    try:
        resultado = eval(formula_avaliada)
    except Exception as e:
        print(f"Erro ao avaliar a fórmula: {e}")
        return None

    return resultado

# Função principal
def main():
    # Solicita ao usuário que insira a fórmula proposicional
    formula = input("Digite a fórmula proposicional (use p, q, r, ~, ^, v, ->, =, ( e ) para as proposições): ")

    # Valida a fórmula inserida
    if not validar_formula(formula):
        print("Fórmula inválida.")
        return

    # Extrai as variáveis da fórmula
    variaveis = sorted(set(re.findall(r'[pqr]', formula)))

    # Gera a tabela verdade
    tabela = gerar_tabela_verdade(variaveis)

    # Avalia a fórmula para cada linha da tabela verdade e armazena os resultados
    resultados = []
    for linha in tabela:
        resultado = avaliar_formula(formula, variaveis, linha)
        if resultado == 0:
            resultado = 'Falso'
        else:
            resultado = 'Verdadeiro'
        resultados.append(linha + [resultado])

    # Imprime a tabela verdade com os resultados
    cabecalho = variaveis + ['Resultado']
    print(tabulate(resultados, headers=cabecalho, tablefmt='grid'))

if __name__ == "__main__":
    main()
