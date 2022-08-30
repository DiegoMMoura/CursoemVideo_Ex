s = 0
for c in range(1, 7):
    n = int(input(f'Please, type the {c} number: '))
    if n % 2 == 0:
        s += n
    else:
        s == 0
print(f'The sum of these numbers are {s}.')
