# Faça um programa que ajude um jogador da MEGA
# SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta
import time
from random import randint
jogo = list()
repeats = list()
repeat = True
n = int(input('How many games do you wanna play? '))
for a in range(0, n):
    for b in range(0, 6):
        number = randint(1, 60)
        while number in repeats:
            number = randint(1, 60)

        jogo.append(number)
        repeats.append(number)
    repeats.clear()

    print(f'Jogo {a+1}:{jogo}')
    time.sleep(0.5)
    jogo.clear()
