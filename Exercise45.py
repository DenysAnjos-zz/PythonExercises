# Crie um programa que faça o computador
# jogar Jokenpô com você
from random import choice

choice0 = input('Choice between Rock, Paper, Scissor:').lower()
choice1 = choice['rock', 'paper', 'scissor']
choice2 = choice(choice1)
if choice0 == 'rock' and choice2 == 'paper':
    print('You Lose!')
elif choice0 == 'rock' and choice2 == 'scissor':
    print('You Win!')
elif choice0 == 'paper' and choice2 == 'scissor':
    print('You Lose!')
elif choice0 == 'paper' and choice2 == 'rock':
    print('You Win!')
elif choice0 == 'scissor' and choice2 == 'rock':
    print('You Lose!')
elif choice0 == 'scissor' and choice2 == 'paper':
    print('You Win!')
else:
    print('Draw!')
