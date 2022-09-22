# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random

win = int(random.choice())
n = int(input('Type a number between 0 and 5:'))
if win == n:
    print('You Win!!!')
else:
    print('You Lose :(')
    print('It was number:', win)