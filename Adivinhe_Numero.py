from random import randint
from time import sleep
print('Estou pensando em um número...\nVamos ver se você consegue acerta!')
n = int(input('Digite um número de 0 a 5: '))
sorte = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if n == sorte:
    print(f'PARABÉNS! Eu estava mesmo pensando no número {sorte}')
else:
    print(f'HA HA HA! Você errou, eu estava pensando no número {sorte}')