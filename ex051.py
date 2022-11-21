print('\033[1;33m=' * 40)
print('{: =^10}'.format('10 numbers from a AP'))
print('=' * 40, '\033[m')
ft = int(input('What is the first number? '))
cd = int(input('What is the common difference? '))
for c in range(ft, ft + (10 * cd), cd):
    print(c, end=' -> ')
print('The End')
