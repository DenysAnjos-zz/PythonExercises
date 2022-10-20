# Crie um programa que gerencie o aproveitamento de
# um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo
# o total de gols feitos durante o campeonato.
soccer = dict()
soccer['name'] = str(input('Name of player:'))
soccer['matches'] = int(input('Number matches:'))
goals = list()

for c in range(0, soccer['matches']):
    n = int(input(f'Number os goals in the match:'))
    goals.append(n)
    soccer['goals'] = goals
    soccer['total'] = sum(goals)
print()
print(soccer)
print()

for i, v in soccer.items():
    print(f'The field {i} has the value {v}.')

print()
print(f'The player {soccer["name"]} played {soccer["matches"]} games.')
for i, v in enumerate(soccer['goals']):
    print(f'In match {i+1}, he did {v}.')
print(f'It was a total of {soccer["total"]} goals.')