from random import randint
from emoji import emojize
from time import sleep
print('{:=^40}'.format('\033[1;34mROCK-PAPER-SCISSOR GAME!\033[m'))
print('''Your options are:
[ 0 ] Rock {}
[ 1 ] Paper {}
[ 2 ] Scissor {}'''.format(emojize(':raised_fist:'), emojize(':crossed_fingers:'), emojize(':raised_hand:')))
itens = ('Rock', 'Paper', 'Scissor')
user = int(input('Please, chose one: '))
if user < 0 or user > 2:
    print('\033[1;31mError! Choose only the options above. Try again.\033[m')
else:
    computer = randint(0, 2)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(0.2)
    print('-=' * 14)
    print(f'The Computer has chosen {itens[computer]}\nYou have chosen {itens[user]}')
    print('-=' * 14)
    if user == computer:
        print(f'It was a draw. Try again.')
    elif user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
        print('You lose... Better luck next time.')
    else:
        print('CONGRATULATIONS!! You win.')
