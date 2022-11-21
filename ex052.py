n = int(input('Please, type any number: '))
qty = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;032m', end=' ')
        qty =+ 1
    else:
        print('\033[034m', end=' ')
    print(c, end=' ')
print(f'\n\033[mThe number {n} is divisible {qty} times.')
if qty == 2:
    print('So it is a PRIME number.')
else:
    print('So it is a REGULAR number.')
