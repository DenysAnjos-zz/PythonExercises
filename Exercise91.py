# Crie um programa onde 4 jogadores joguem um
# dado e tenham resultados aleatórios. Guarde
# esses resultados em um dicionário. No final,
# coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
game = {'player1': randint(0, 6), 'player2': randint(0, 6),
        'player3': randint(0, 6), 'player4': randint(0, 6)}
print('Drawn values:')
for v, i in game.items():
    print(f'{v} has {i} on the dice')
    sleep(0.5)
sleep(1)
print('Ranking!!!')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'In {i+1}° place {v[0]} with {v[1]}.')
    sleep(0.5)
