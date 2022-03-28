import random
import time
from time import sleep
num = random.randint(0,5)

num2 = int(input('Digite um numero e veja se foi o mesmo escolhido pela maquina:'))
print('Processando...')
time.sleep(2)
if num == num2:
    print('Parabéns, você venceu o computador')
else:
    print('O computador venceu')
