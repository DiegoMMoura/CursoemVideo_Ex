d = int(input('For how many days did you rent the car? '))
km = float(input('How many kilometers did you drive? '))
p = (d * 60) + (km * 0.15)
print(f'The total amount to be paid is: BRL {p:.2f}')
