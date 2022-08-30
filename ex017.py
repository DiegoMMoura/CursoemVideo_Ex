from math import hypot
co = float(input('Please, inform the opposite cateto: '))
ca = float(input('Please, inform the adjacent cateto: '))
hy = hypot(co, ca)
print(f'The hypotenuse is {hy:.2f}.')
