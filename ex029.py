v = float(input('What is the speed of the vehicle? '))
#if v <= 80:
#    print(f'Have a nice day. Drive safe!')
#else:
#    print(f'TAX DRIVE FEE! You have exceed the speed limit of 80Km/h. \nYour tax fee is R${((v - 80) * 7):.2f}.')
if v >= 80:
    print(f'TAX DRIVE FEE! You have exceed the speed limit of 80Km/h. \nYour tax fee is R${((v - 80) * 7):.2f}.')
print('Have a nice day. Drive safe!')
