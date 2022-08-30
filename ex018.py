from math import radians, sin, cos, tan
#import math
a = float(input('Type any angle: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'The angle of {a} has a SINE of {s:.2f}.')
print(f'The angle of {a} has a COSINE of {c:.2f}.')
print(f'the angle of {a} has a TANGENT of {t:.2f}')
