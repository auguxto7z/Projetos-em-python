ano = int(input("Em que ano estamos? "))
nasc = int(input("Em que ano você nasceu? "))
idade = (ano - nasc)
print(f'Em {ano} você tem {idade} anos.')
if idade >= 18:
    print('E você é maior de idade!')
else:
    print("E você é menor de idade!")