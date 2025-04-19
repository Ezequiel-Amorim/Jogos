from random import choice
from time import sleep
def ln ():
    print('-=-'*10)
    

ln()
print('Jogo do Pedra,Papel e Tesoura | Duelo de computadores')
ln()
jogo = ['Pedra','Papel','Tesoura']
sleep(1)
player = choice(jogo)
sleep(1)
computador = choice(jogo)
ln()
print(f'Player jogou : {player} | Computador jogou : {computador}')
ln()

def vencedor(player, computador):
    if player == computador:
        print('Empate!')
    elif (player == 'Pedra' and computador == 'Tesoura') or \
         (player == 'Papel' and computador == 'Pedra') or \
         (player == 'Tesoura' and computador == 'Papel'):
        print(f'{player} ganha de {computador} - Player venceu!')
    else:
        print(f'{computador} ganha de {player} - Computador venceu!')


vencedor(player,computador)
