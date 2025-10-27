largura = 30
print ('=' * largura)
print ('COLÉGIO ROTARY' . center (largura))
print('=' * largura)

n1 = float(input('Primeira Nota: '))
n2 = float (input('Segunda Nota: '))
s = (n1+n2)  / 2
print('=' * 30)
print(f'MÉDIA: {s:.1f}')
if s >= 5:
	print('ALUNO APROVADO')
else:
	print('ALUNO REPROVADO')
print('=' * 30)
