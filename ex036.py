hv = float(input('What is the value of the house/apartment? '))
s = float(input('How much do you earn monthly? '))
y = int(input('How many year do you wish to pay for the house/apartment? '))
mp = ((hv / 12) / y)
if mp <= (s * 0.3):
    print(f'Congratulations!! Your financing payment has been approved by the bank and your monthly payment is {mp:.2f}.')
else:
    print('Unfortunately, your financing has ben denied by the bank. My apologies.')
