emprestimo = int(input('Qual valor do empréstimo? '))
parcela = int(input('Quantas parcelas? '))
emprestimo = emprestimo * 1.20
total = (emprestimo/parcela) 
print(f'Vou pagar {parcela} parcelas de R${total}')