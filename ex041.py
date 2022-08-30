from datetime import date
now = date.today().year
y = int(input('Please, inform the year of yur birth: '))
age = now - y
print(f'The athlete has {age} years old')
if age <= 9:
    print('Classification: Mirim.')
#elif age > 9 and age <= 14:
elif age <= 14:
    print('Classification: Infantil.')
#elif age > 14 and age <= 19:
elif age <= 19:
    print('Classification: Junior.')
#elif age > 19 and
elif age <= 25:
    print('Classification: Senior.')
else:
    print('Classification: Master.')
