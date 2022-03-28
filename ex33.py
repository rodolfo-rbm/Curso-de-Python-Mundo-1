'''Faça um programa que leia 3 números
e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('DIgite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))

if n1 > n2:
    maior = n1
elif n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

print('{} é o maior número.'.format(maior))

if n1 < n2:
    menor = n1
elif n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

print('{} é o menor número.'.format(menor))
