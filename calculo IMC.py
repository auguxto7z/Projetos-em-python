M = float(input('Massa (kg) : '))
A = float(input('Altura (m) : '))
IMC = M / (A * A)
print(f'IMC : {IMC: .2f}')
if IMC <= 17:
	print('Muito abaixo do peso')
elif (IMC >= 17) and (IMC <= 18.5):
	print('Abaixo do Peso')
elif (IMC >= 18.5) and (IMC < 25):
	print('Peso ideal')
elif (IMC >= 25) and (IMC < 30):
	print('Sobrepeso')
elif (IMC >= 30) and (IMC < 35):
	print('Obesidade')
elif (IMC >= 35) and (IMC < 40):
	print('Obesidade severa')
else:
	print('Obesidade Morbida')
