'''Desenvolva um programa que pergunte a distancia
de uma viagem em KM. Calcule o preço da passagem,
cobrando R$ 0,50 por KM para viagens de até 200Km
e R$ 0,45 para viagens mais longas'''

distancia = float(input('Digite a distância da viagem que irá fazer: '))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('Para  viajar {:.0f} Km você irá gastar R$ {:.2f}'.format(distancia, valor))

