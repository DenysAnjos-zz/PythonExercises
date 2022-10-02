# Faça um programa que jogue par ou ímpar com o
# computador. O jogo só será interrompido quando
# o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint

choose = ''
victories = total = 0
check = int
check = 0

while check == 0:
    number = int(input('Type a number:'))
    choose = str(input('Choose between pair or odd:')).lower()
    computer = randint(0, 10)
    total = computer + number
    if total % 2 == 0 and choose == 'pair':
        victories += 1
        check = 0
    elif total % 2 == 0 and choose == 'odd':
        check = 1
    else:
        check = 1

    print('You choose {} and the computer'
          ' {}. The total is {}.'.format(number, computer, total))

print('You Lose!')
print('You won {} times in a row.'.format(victories))
