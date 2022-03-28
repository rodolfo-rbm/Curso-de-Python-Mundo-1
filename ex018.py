from math import sin, cos, tan, radians

num = float(input('Digite o angulo: '))

print('O angulo {:.2f}º tem cosseno de {:.2f} seno de {:.2f} e tangente de {:.2f}'.format(num, cos(radians(num)), sin(radians(num)), tan(radians(num))))
