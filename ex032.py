from datetime import date
y = int(input('Hello, please inform the year: '))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f'The year {y} is a leap year.')
else:
    print(f'The year {y} is not a leap year.')
