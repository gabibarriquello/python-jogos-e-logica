from random import randint
print('=' *5, 'Vamos Jogar Jokenpo', '=' * 5)
jogador = int(input(('''Escolha a sua Jogada
[ 1 ] Pedra 
[ 2 ] Papel 
[ 3 ] Tesoura: ''')))
computador = randint(1,3)
if jogador == 1 and computador == 2:
   print(f'VOCÊ VENCEU. Eu escolhi {computador}')
elif jogador == 2 and computador == 3:
    print(f'EU VENCI. Eu escolhi {computador}')
elif jogador == 3 and computador == 1:
    print(f'EU VENCI. Eu escolhi {computador}')
elif jogador == 1 and computador == 3:
    print(f'VOCÊ VENCEU. Eu escolhi {computador}')
elif jogador == 2 and computador == 1:
    print(f'VOCÊ VENCEU. Eu escolhi {computador}')
elif jogador == 3 and computador == 2:
    print(f'VOCÊ VENCEU. Eu escolhi {computador}')
elif jogador == computador:
    print(f'Nós temos um empate. Eu escolhi {computador}')