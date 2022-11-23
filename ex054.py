from datetime import date
year_low = 0
year_high = 0
for c in range(1, 4 ):
    ano = int(input(f'What year the {c}º person was born? '))
    today = date.today().year
    if today - ano < 21:
        year_low += 1
    else:
        year_high += 1
print(f'There are {year_low} person(s) under age.')
print(f'There are {year_high} person(s) of legal age')
