import ttg

# Ordem de Precedência: ~, and, or

# Exemplo 01
ex_01 = ttg.Truths(['p', 'q'],['p and q'],  ints=False)
                   
print(ex_01)

# Exemplo 02
ex_02 = ttg.Truths(['p'],['~p'], ints=False)	

print(ex_02)

# Exemplo 03
ex_03 = ttg.Truths(['p'],['~(~p)'], ints=False)	

print(ex_03)
