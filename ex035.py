color = {'none': '\033[m',
         'blue': '\033[34m',
         'red': '\033[31m'}
print('-='.format(color['blue']) * 25)
print(' ' * 15 + 'TRIANGLE ANALYZER')
print('-='.format(color['blue']) * 25)
l1 = float(input('Please, inform the first triangle side number: '))
l2 = float(input('Please, inform the second triangle side number: '))
l3 = float(input('Please, inform the third triangle side number: '))
if l1 > abs(l2 - l3) and l1 < (l2 + l3):
    print('These side numbers CAN make a triangle')
else:
    print('These side numbers CAN NOT make a triangle.')
