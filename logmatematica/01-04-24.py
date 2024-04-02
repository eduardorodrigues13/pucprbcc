import ttg

ex_1 = ttg.Truths(['p', 'q'], ['p and q', 'p or q'], ints=False)
print(ex_1)
print()
print(ex_1.valuation())