print('Please, choose two int. numbers:')
n1 = int(input('First Number: '))
n2 = int(input('Second number: '))
if n1 > n2:
    print(f'The first number {n1} is greater than the second one {n2}.')
elif n1 < n2:
    print(f'The second number {n2} is greater than the first one {n1}.')
else:
    print('Both value are the same.')
