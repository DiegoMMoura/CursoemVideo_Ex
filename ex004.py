n1 = input('Type anything: ')
n2 = type(n1)
print(f'The primitive class for it is: {n2}.')
print(f'Is it number and letter? {n1.isalnum()}.')
print(f'Is there space? {n1.isspace()}.')
print(f'Is it a number? {n1.isnumeric()}.')
print(f'Is there capital letter? {n1.isupper()}.')
print(f'Is there no capital letter? {n1.islower()}.')
print(f'Is it only letter ? {n1.isalpha()}.')
