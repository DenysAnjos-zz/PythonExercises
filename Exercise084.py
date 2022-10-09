# Faça um programa que leia nome e peso
# de várias pessoas guardando tudo em
# uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas.
# Um listagem com as pessoas mais leves.
id = list()
group = list()
highWeight = lowWeight = totalPeople = 0
while True:
    id.append(str(input('Type your name:')))
    id.append(int(input('Type your weight:')))
    group.append(id[:])
    id.clear()
    totalPeople += 1
    check = str(input('Do you want continue?(y/n)'))
    if check in 'nN':
        break
for n in group:
    if n[1] >= 80:
        print(f'High height:{n[0]}')
    if n[1] <= 60:
        print(f'Light weight:{n[0]}')
print(f'Total people registered:{totalPeople}')