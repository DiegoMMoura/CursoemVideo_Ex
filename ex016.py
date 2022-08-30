#import math
from math import trunc
v = float(input('type any value: '))
#print(f'The value typed is {v} and his whole fraction is {v//1:.0f}.')
#print(f'The value typed is {v} and his whole fraction is {int(v)}.')
print(f'The value typed is {v} and his whole fraction is {trunc(v)}.')
