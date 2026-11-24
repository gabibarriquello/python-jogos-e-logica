from random import randint
palpites = 1
print('Estou pensando em um número entre 0 e 10\nVocê consegue adivinhar?')
jogador = int(input('Digite o número que eu estou pensando: '))
computador = randint(0, 10)
while jogador != computador:
      jogador = int(input('AH que pena você errou.Tente de novo: '))
      if jogador == computador:
          print(f'PARABÉNS! Você acertou\nEu estava mesmo pensando no número {computador}')
      palpites += 1
print(f'Você precisou de {palpites} palpites para acertar')
