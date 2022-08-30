from random import choice
a = input('First student: ')
b = input('Second student: ')
c = input('Third student: ')
d = input('Fourth student: ')
lista = [a, b, c, d]
print(f'The student chosen is {choice(lista)}')
