n = int(input('Please, type any number: '))
count = 0
plus = 0
for c in range(1, n+1):
    count += 1
    if c % count == 0 >2:
        print('regular number')
    else:
        print('prime number')
