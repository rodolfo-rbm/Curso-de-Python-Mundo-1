dia = float(input('Por quantos dias o carro foi alugado ? '))
km = float(input('Qual foi a quilomotragem rodada nesse periodo? '))

total = (dia*60)+(0.15*km)

print('O total a pagar por {} dias e por ter rodado {:.2f}km é de R${:.2f}'.format(dia, km, total))
