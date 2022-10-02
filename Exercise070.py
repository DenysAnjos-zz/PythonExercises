# Crie um programa que leia o nome e o
# preço de vários produtos. O programa
# deverá perguntar se o usuário vai
# continuar. No final mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato.
cheapest2 = ''
total = over1000 = cheapest = 0

while True:
    price = int(input('Type the value:'))
    name = str(input('Type the product name:'))
    total += price

    if cheapest == 0:
        cheapest = price
        cheapest2 = name
    if price > 1000:
        over1000 += 1
    if price < cheapest:
        cheapest2 = name

    check = input('Do you want continue?(y/n)').lower()
    if check == 'n':
        break

print('Total value:', total)
print('Products over R$1000:', over1000)
print('Cheapest product name:{}, value:R${}'.format(cheapest2, cheapest))
