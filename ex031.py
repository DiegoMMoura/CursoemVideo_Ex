d = float(input('What is the distance of your trip (in Km)? '))
print(f'You are about to start a trip of {d}Km.')
#p = d * 0.5 if d <= 200 else d * 0.45
if d <= 200:
    p = d * 0.5
#    print(f'And the cost of the trip to {d}Km is R${(d * 0.5):.2f}.')
else:
    p = d * 0.45
#    print(f'And the cost of the trip to {d}Km is R${(d * 0.45):.2f}.')
print(f'And the cost of your ticket is R${p:.2f}')
