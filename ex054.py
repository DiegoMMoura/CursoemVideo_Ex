from datetime import date
ano = 0
for c in range(0, 3):
    ano = int(input(f'What year the {c} person was born? '))
today = date.now()
print(today)
#   if ano <= (today + 18):
#        print()
