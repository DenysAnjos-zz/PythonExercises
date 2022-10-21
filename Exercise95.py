# Aprimore o desafio 93 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.
team = list()
player = dict()
match = list()
while True:
    player.clear()
    player['name'] = str(input('Name of player:'))
    tot = int(input(f'How many matches he play?'))
    match.clear()
    for c in range(0, tot):
        match.append(int(input(f'Number os goals in the match:')))
    player['goals'] = match[:]
    player['total'] = sum(match)
    team.append(player.copy())
    check = str(input('Do you wanna continue?(y/n)'))
    if check in 'Nn':
        break
for i in player.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(team):
    print(f'{k}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    check = int(input('Do want to see details of which player?(999 to stop)'))
    if check == 999:
        break
    else:
        for i, v in enumerate(team[check]['goals']):
            print(f'In match {i+1} he did {v}')
