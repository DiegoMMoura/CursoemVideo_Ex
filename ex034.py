s = float(input('What is the salary of te employ? '))
if s <= 1250:
    ns = (s * 0.15) + s
else:
    ns = (s * 0.10) + s
print(f'For those who win R$ {s:.2f} will win from now on RS$ {ns:.2f}.')
