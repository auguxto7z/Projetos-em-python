while True:
  print('''[1] Para somar.
[2] Para dividir.
[3] Para multiplicar.
[4] Para Subtrair.
[5] Para sair''')
  opc = input('Digite um valor numerico: ')

  if opc == '5':
    print('finalizando ...')
    break

  elif opc == '1':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    print(f'A soma entre {a} + {b} = {a+b}')
    
  elif opc == '2':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    print(f'A divisão entre {a} / {b} = {a/b}')
  
  elif opc == '3':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    print(f'A multiplicação entre {a} * {b} = {a*b}')
    
  elif opc == '4':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    print(f'A subtração entre {a} - {b} = {a-b}')
  
  else:
    print('Opção inválida! Digite um número de 1 a 5.')