# Melhore o jogo do desafio 028 onde o
# computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar,
# mostrando no final quantos palpites
# foram necessários para vencer
from random import randint
computer = randint(0, 5)
count, check = 0, 0
while check != computer:
    check = int(input('Type a number:'))
    count += 1
print('You win!\nAnd tried {} times'.format(count))
