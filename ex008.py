n = float(input('Type the height or the distance in meters: '))
k = n/1000
h = n/100
da = n/10
dm = n*10
cm = n*100
mm = n*1000
print(f'The same value of {n} meters are:')
print(f'{k} Km \n{h} Hm \n{da} Dam \n{dm} Dm \n{cm:.0f} Cm \n{mm:.0f} mm')
