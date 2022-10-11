# Faça um programa que leia nome e peso
# de várias pessoas guardando tudo em
# uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas.
# Um listagem com as pessoas mais leves.
id = list()
group = list()
highWeight = lightWeight = 0
while True:
    id.append(str(input('Type your name:')))
    id.append(float(input('Type your weight:')))
    if len(group) == 0:
        highWeight = lightWeight = id[1]
    else:
        if id[1] > highWeight:
            highWeight = id[1]
        if id[1] < lightWeight:
            lightWeight = id[1]
    group.append(id[:])
    id.clear()
    check = str(input('Do you want continue?(y/n)'))
    if check in 'nN':
        break
print(f'Biggest weight:{highWeight}KG. Name:', end='')
for h in group:
    if h[1] == highWeight:
        print(f'[{h[0]}] ', end='')
print()
print(f'Lowest weight:{lightWeight}KG. Name:', end='')
for h in group:
    if h[1] == lightWeight:
        print(f'[{h[0]}] ', end='')
print()
print(f'Total people registered:{len(group)}')
