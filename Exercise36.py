# Escreva um programa para aprovar o empréstimo
# bancario para a compra de uma casa. O programa
# vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo
# que ela não pode exceder 30% do salário ou
# então o empréstimo será negado
valueHouse = float(input('Type the house value:'))
salary = float(input('Type your salary:'))
years = int(input('Years to pay:'))
if salary/(30/100) < valueHouse/(years*12):
    print('Denied!')
else:
    print('Approved!')
