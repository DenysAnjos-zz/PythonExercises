# Faça um programa que ajude um jogador da MEGA
# SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta
from time import sleep
from random import randint
numbers = list()
plays = list()
tot = 1
quant = int(input('How much games do you wanna play?'))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in numbers:
            numbers.append(num)
            cont += 1
        if cont >= 6:
            break
    numbers.sort()
    plays.append(numbers[:])
    numbers.clear()
    tot += 1
for n in range(0, quant):
    print(f'Game: {plays[n]}')
    sleep(0.5)