import random

nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input("Nome do segundo aluno: "))
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')

lista = [nome1, nome2, nome3, nome4]

print('O aluno sorteado é {}'.format(random.choice(lista)))


