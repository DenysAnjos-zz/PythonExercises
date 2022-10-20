# Crie um programa que leia nome, sexo e idade de várias
# pessoas, guardando os dados de cada pessoa num dicionário
# e todos os dicionários numa lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
person = dict()
people = list()
average = 0
while True:
    person['name'] = str(input('Name: '))
    person['age'] = int(input('Age: '))
    average += person['age'] / 2
    person['sex'] = str(input('Sex:(M/W): ')).lower()[0]
    people.append(person.copy())
    check = str(input('Do you want continue?(y/n)'))
    if check in 'Nn':
        break

print(f'Total people registered:{len(people)}')
print(f'Average age {average}')
print('List of women:')
for p in people:
    if p['sex'] in 'wW':
        print(f'{p["name"]}', end='')
print('Above average people:')
for a in people:
    if a['age'] > average:
        print(f'{a["name"]}', end='')
