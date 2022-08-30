n = int(input('Please, type any int. number: '))
print('''Chose one of the folowing convert choices:
[ 1 ] Convert to Binary
[ 2 ] Convert to Octal
[ 3 ] Convert to Hexadecimal''')
c = int(input('Wight choice do you want? '))
if c == 1:
    print(f'{n} converted to Binary is: {bin(n)[2:]}.')
elif c == 2:
    print(f'{n} converted to Octal is: {oct(n)[2:]}.')
elif c == 3:
    print(f'{n} converted to Hehadecimal is: {hex(n)[2:]}.')
else:
    print('Invalid option. Please, try again.')
