# Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, crie
# duas listas extras que vão conter apenas
# os valores pares e os valores ímpares
# digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.
numbers = list()
numbersOdd = list()
numbersPair = list()
for c in range(0, 5):
    n = int(input('Type a number:'))
    numbers.append(n)
    if n % 2 == 0:
        numbersOdd.append(n)
    else:
        numbersPair.append(n)
    check = str(input('Do you want continue?(y/n)')).lower()
    if check in 'nN':
        break
print('Numbers:', numbers)
print('Pairs:', numbersPair)
print('Odds:', numbersOdd)
