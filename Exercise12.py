# Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto
product = float(input('Type a product value:R$'))
print('The descounted product is: R${:.2f}'.format(product-(product*(5/100))))