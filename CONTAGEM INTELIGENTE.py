from time import sleep
print('=' * 30)
print('''    CONTAGEM INTELIGENTE''')
print('=' *  30)
cont = int(input('Inicio: '))
d = int(input('Fim: '))
x = 0
print('=' * 30)
print('''       C O N T A N D O''')
print('=' *  30)
if cont < d:
	for x in range(cont, d +1):
	  print(x)
	  sleep(0.5)
else:
	for x in range (cont, d -1 , -1):
	  print(x)
	  sleep(0.5)
print('\n' + '-' * 30)
print(f'{"FIM!":^30}')
print('-' * 30)