from math import hypot

cat_opo = float(input('Digite o cateto oposto do triangulo: '))
cat_adj = float(input('Digite o cateto adjacente do triangulo: '))

print('O valor da hipotenusa é {}'.format(hypot(cat_opo, cat_adj)))

