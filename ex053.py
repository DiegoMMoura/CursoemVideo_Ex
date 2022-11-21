frase = (input('Please, type any frase: ')).strip()
reverse_frase = frase[::-1]
frase = frase.replace(" ","")
reverse_frase = reverse_frase.replace(" ","")
print(f'The inverse of {frase.upper()} is {reverse_frase.upper()}.')
if frase == reverse_frase:
    print('It is a Palindrome.')
else:
    print('It is not a Palindrome.')
