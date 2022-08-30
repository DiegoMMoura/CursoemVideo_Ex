from datetime import date
now = date.today().year
y = int(input('What year were you born? '))
print(f'Who was born in {y} has {now - y} years old in {now}.')
print('''What is your genre?
Please type [M] for male
Please, type [F] for female''')
g = str(input('')).upper().strip()
if g == 'F':
    print('The application in the Military Services is not mandatory.')
elif g == 'M' and now - y < 18:
    print(f'It is remaining {18 - (now - y)} years for you to apply the Military Services.')
    print(f'The year of your application will be {now + (18 - (now - y))}.')
elif g == 'M' and now - y > 18:
    print(f'You should have applied to the Military Services {(now - y) - 18} year ago.')
    print(f'The year of your application was {now - ((now - y) - 18)}')
elif g == 'M' and now == 18:
    print('WARNING! You should apply to the Military Services IMMEDIATELY.')
elif g != 'M' or 'F':
    print('Please, inform again your genre.\n Use [M] for male or [F] for Female.')
