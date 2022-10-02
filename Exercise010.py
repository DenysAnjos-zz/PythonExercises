# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar, considere U$ 1.00 = R$3.27#
money = float(input("How many reais you have?R$"))
print("You have U${:.2f} dollars".format(money/3.27))
