''' Faça um programa que leia uma frase pelo teclado
 e mostre quantas vezes aparece a letra “A”, em que
 posição ela aparece a primeira vez e em que posição
 ela aparece a última vez.'''

frase = str(input('Digite uma frase qualquer: ')).strip().lower()

print('A letra A aparece {} vez(ez) '.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('a')))
