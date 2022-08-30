from random import randint
from time import sleep
print('-=--=' * 10)
print('I will pick a number from 0 to 5. Try to guess...')
print('-=--=' * 10)
n1 = int(input('What number is it? '))
n2 = randint(0, 5)
print('THINKING...')
sleep(3)
if n1 == n2:
    print('CONGRATULATION!! You bit me.')
else:
    print(f'I WIN! I chose the number {n2}, not {n1}.')
