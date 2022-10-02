# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela está o time do Atlético-MG
teams = ('Palmeiras', 'Internacional', 'Fluminense',
         'Corinthians', 'Flamengo', 'Atletico-PR',
         'Atletico-MG', 'América-MG', 'Fortaleza',
         'Botafogo', 'Santos', 'Goiás', 'São Paulo',
         'Bragantino', 'Curitiba', 'Avai',
         'Atletico-GO', 'Juventude')

print('All teams:', teams)
print('-' * 100)
print('Top five:', teams[0:5])
print('-' * 100)
print('The last four:', teams[-4:])
print('-' * 100)
print('In alphabetic order:', sorted(teams))
print('-' * 100)
print(f'Atlético-MG is in {teams.index("Atletico-MG")+1} place.')
