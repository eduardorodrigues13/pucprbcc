i = 1
j = 1

while i < 11:
    if j < 11:
        print(f'{i} x {j} = {i*j}')
        j += 1
    else:
        i += 1
        j = 1