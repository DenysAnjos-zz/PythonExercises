# Crie um programa que vai ler vários números e
# colocar em lista. Depois disso, mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista

numbers = list()
quantity = 0
check5 = 'No'
while True:
    numbers.append(int(input('Type a number:')))
    if numbers[quantity] == 5:
        check5 = 'Yes'
    quantity += 1
    check = str(input('Do you want continue?(y/n)'))
    if check in 'nN':
        break

numbers.sort(reverse=True)
print('Typed numbers:', quantity)
print('Numbers reverse:', numbers)
print('Number 5 was on the list?', check5)