n = str(input('Type your full name: ')).strip()
fn = n.split()
print('Nice to meet you.')
print(f'Your first name is {fn[0]}.')
print(f'Your last nae is {fn[len(fn)-1]}')
