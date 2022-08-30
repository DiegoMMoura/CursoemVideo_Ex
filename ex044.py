print('{:=^40}'.format(' LOJAS MELO MOURA '))
p = float(input('What is the net price of your product? '))
print('''WAYS OF PAYMENT
[ 1 ] Cash in Advance with money or check
[ 2 ] 1x with Credit Card
[ 3 ] 2X with Credit Card
[ 4 ] 3X or more with Credit Card''')
option = int(input('Please, choose the payment way: '))
if option == 1:
    total = p - (p * 0.1)
#    print(f'Your purchase of R$ {p:.2f} will cost {total:.2f}.')
elif option == 2:
    total = p - (p * 0.05)
#    print(f'Your purchase of R$ {p:.2f} will cost {total:.2f}')
elif option == 3:
    total = p
    print(f'You will pay it in 2 times of R${(p / 2):.2f}. No fee will be applied.')
elif option == 4:
    qty = int(input('How many times you will split the payment with the credit card? '))
    if qty == 1:
        total = p - (p * 0.05)
#        print(f'Your purchase of R$ {p:.2f} will cost {(p - (p * 0.05)):.2f}.')
    elif qty == 2:
        total = p
        print(f'You will pay it in 2x of R${(p / 2):.2f}. No fee will be applied.')
#        print(f'You will pay it in {qty} times of R${p:.2f}.')
#        print(f'Your purchase of R${p:.2f} will not have any fee.')
    else:
        total = p + (p * 0.2)
        print(f'You will pay it in {qty}x of R${(total / qty):.2f} with fee.')
#        print(f'Your purchase of R${p:.2f} will cost R${total:.2f}.')
else:
    total = p
    print('\033[1;31mTry again. Please choose one of the options above.\033[m')
print(f'Your purchase of R$ {p:.2f} will cost {total:.2f}.')
