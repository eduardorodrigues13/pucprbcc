import ttg

#Exercício a) p ^ q v ~p

ex_a1 = ttg.Truths(['p', 'q'], ['p and q or ~p'], ints=False)
print(ex_a1)

#Exercício b) p -> q = ~p v q
ex_b1 = ttg.Truths(['p', 'q'], ['p and q = ~p or q'], ints=False)
print(ex_b1)

#Exercício f) ~(((~q)^p)^(~q))=(p->(~q)))
ex_f1 = ttg.Truths(['p', 'q'], ['not(not q and p and not q = p => not q)'], ints=False)
print(ex_f1)