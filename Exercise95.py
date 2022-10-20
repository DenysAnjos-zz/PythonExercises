# Aprimore o desafio 93 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.
soccer = dict()
goals = list()
while True:
    soccer['name'] = str(input('Name of player:'))
    soccer['matches'] = int(input('Number matches:'))
    for c in range(0, soccer['matches']):
        n = int(input(f'Number os goals in the match:'))
        goals.append(n)
        soccer['goals'] = goals
        soccer['total'] = sum(goals)
        check = str(input('Do you wanna continue?(y/n)'))
        if check in 'Nn':
            break
