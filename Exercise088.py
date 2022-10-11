# Faça um programa que ajude um jogador da MEGA
# SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta
import time
from random import randint
numbers = list()
repeats = list()
n = int(input('How many games do you wanna play? '))
for column in range(0, n):
    for line in range (0, 3):
