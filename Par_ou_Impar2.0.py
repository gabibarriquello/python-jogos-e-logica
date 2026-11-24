from random import randint
print('-='*10)
print('Vamos Jogar PAR ou IMPAR')
print('-='*10)
cont = 0
escolha = ''
jogador = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    computador = randint(0,10)
    soma = jogador + computador
    if soma % 2 == 0 and escolha == 'I':
         print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {soma} PAR ')
         print('Ah que pena...VOCÊ PERDEU!!!')
         break
    elif soma % 2 != 0 and escolha == 'P':
        print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {soma} IMPAR')
        print('Ah que pena...VOCÊ PERDEU!')
        break
    elif soma % 2 != 0 and escolha == 'I':
        print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {soma} IMPAR')
        print('VOCÊ GANHOUU!!!')
        print('Vamos jogar novamente...')
        print('-'*20)
        cont += 1
    elif soma % 2 == 0 and escolha == 'P':
        print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {soma} PAR')
        print('VOCÊ GANHOUU! ')
        print('Vamos jogar novamente...')
        print('-' * 20)
        cont += 1
print('-='*10)
print(f'GAME OVER!!! Você ganhou {cont} vezes')
