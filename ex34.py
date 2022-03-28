'''Escreva um programa que pergunte um
salário de um funcionário e calcule o valor
do seu aumento. P/ salários acima de R$ 1250.00,
calcule um aumento de 10%.
P/ salários abaixo ou igual a R$ 1250.00,
o aumento é de 15%.'''

sal = float(input('Digite o seu salário: R$ '))

if sal > 1250.00:
    print('Parabéns você receberá um aumento de 10%.')
    print('Com o aumento o seu salário agora é de R$ {:.2f}'.format(sal*1.1))
elif sal <=1250.00:
    print('Parabéns você receberá um aumento de 15%.')
    print('Com o aumento o seu salário agora é de R$ {:.2f}'.format(sal*1.15))
