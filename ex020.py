from random import shuffle
a = input('First student name: ')
b = input('Second student name: ')
c = input('Third student name: ')
d = input('Fourth student name: ')
lista = [a, b, c, d]
shuffle(lista)
print(f'The order of the presentation is: \n{lista}.')
