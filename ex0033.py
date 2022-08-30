v1 = int(input('Please, type the first value: '))
v2 = int(input('Please, type the second value: '))
v3 = int(input('Please, type the third value: '))
#lista = [v1, v2, v3]
#print(f'The lower value is {min(lista)}. \nThe higher value is {max(lista)}.')
menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v2
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'The lower value is {menor} and the higher value is {maior}.')
