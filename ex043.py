p = float(input('Please, inform your weight (in kilos): '))
a = float(input('Please, inform your height (in meters): '))
imc = p / (a**2)
print(f'The IMC is {imc:.1f}')
if imc < 18.5:
    print('BE CAREFUL, you are under weight.')
#elif imc >= 18.5 and imc < 25:
elif 18.5 <= imc < 25:
    print('CONGRATULATION, you are at your ideal weight.')
#elif imc >= 25 and imc < 30:
elif 25 <= imc < 30:
    print('BE CAREFUL, you are over weight.')
#elif imc >= 30 and imc < 40:
elif 30 <= imc < 40:
    print('WARNING, you are consider obese.')
else:
    print('MEDICAL SITUATION. Look for an specialist. ')
