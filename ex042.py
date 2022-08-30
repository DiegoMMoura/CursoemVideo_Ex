print('-=' * 25)
print(' ' * 15 + 'TRIANGLE ANALYZER')
print('-=' * 25)
l1 = float(input('Please, inform the first triangle side number: '))
l2 = float(input('Please, inform the second triangle side number: '))
l3 = float(input('Please, inform the third triangle side number: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('These side numbers CAN make a triangle ', end='')
    if l1 == l2 == l3:
        print('EQUILATERAL.')
    elif l1 != l2 != l3 != l1:
        print('SCALENE.')
    else:
        print('ISOSCELES.')
else:
    print('These side numbers CAN NOT make a triangle.')
