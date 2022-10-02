# Melhore o jogo do desafio 028 onde o
# computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar,
# mostrando no final quantos palpites
# foram necessários para vencer
from random import randint
computer = randint(0, 10)
check = int(input('Try to guess a number between 0 to 10:'))
count = 1
while check != computer:
    check = int(input('Try again:'))
    count += 1
print('You win!\nYou tried {} times'.format(count))
