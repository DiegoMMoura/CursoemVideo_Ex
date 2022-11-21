frase = str(input('Please, type an frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'The inverso of {junto} is {inverso}.')
if inverso == junto:
    print('It is a palindrome.')
else:
    print('It is not a palindrome')
