g1 = float(input('Please, inform your first grade: '))
g2 = float(input('Please, inform your second grade: '))
gf = (g1 + g2) / 2
print(f'With the first grade {g1:.1f} and the second grade {g2:.1f}, yur final grade is {gf:.1f}.')
if gf < 5:
    print('You have failed.')
elif gf >= 5 and gf < 7:
    print('You are in recuperation.')
else:
    print('Congratulation! You have been approved.')
