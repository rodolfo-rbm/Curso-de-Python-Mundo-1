vel = float(input('Digite a velocidade atual do carro: '))

if vel < 80:
    print('Você está dentro do limite de veolcidade:')
else:
    multa = (vel - 80)*7
    print('Atenção!!! Você ultrapassou o limite de Velocidade!!!')
    print('Consequentemente você foi multado em R$ {:.2f}'.format(multa))
