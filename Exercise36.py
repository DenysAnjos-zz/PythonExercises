# Escreva um programa para aprovar o empréstimo
# bancario para a compra de uma casa. O programa
# vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo
# que ela não pode exceder 30% do salário ou
# então o empréstimo será negado
valueHouse = float(input('Type the house value:R$'))
salary = float(input('Type your salary:R$'))
years = int(input('Years to pay:'))
inst = valueHouse/(years*12)
if salary*30/100 < inst:
    print('Denied!')
else:
    print('Approved!')
