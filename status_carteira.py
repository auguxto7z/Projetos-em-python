print('=' * 30)
print(''' DEPARTAMENTO DE TRANSITO''')
print('=' *  30)


ano = int(input('Ano Atual (yyyy): '))
nasc = int(input('Ano de Nascimento (yyyy): '))
JP = (ano-nasc)


largura = 30
print ('=' * largura)
print ('STATUS' . center (largura))
print('=' * largura)

print(f'IDADE : {JP} anos')
if JP  >= 18:
	print('APTO PARA TIRAR A CARTEIRA')
else:
	print('INAPTO PARA TIRAR A CARTEIRA')
print('=' * 30)

print('*******FIM DA EXECUÇÃO*******')