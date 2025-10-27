def linha(nome):
    print('=-' * 15)
    print(f'       {nome}')
    print('=-' * 15)

linha('📘 COLÉGIO ROTARY')
linha('--Sistemas de Notas--')

maior = 0
n = ''

while True:
    al = input('Quantos alunos tem na turma? ')
    if al.isdigit():
        al = int(al)
        if al > 0:
            break
    print('❌ Valor inválido! Digite apenas números inteiros.')

print('=-' * 15)
for x in range(1, al + 1):
    print(f'ALUNO {x}')
    a = input('Nome do aluno: ')

        while True:
        nota = input(f'Nota de {a}: ')
        try:
            b = float(nota)
            if 0 <= b <= 10:
                break
            else:
                print('⚠️ A nota deve ser entre 0 e 10.')
        except ValueError:
            print('⚠️ Coloque uma nota válida (somente números).')

    print('=-' * 15)

    if b > maior:
        maior = b
        n = a

print(f'A maior nota da sala foi a de {n} com nota {maior}')
#AUGUSTO PIROCUDO 18CM#
#@AUGUSTO PIKA DE ELEFANTE#