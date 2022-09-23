# Desenvolva uma lógica que leia
# o peso e altura de uma pessoa,
# calcule o imc e mostre seu status,
# de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
wei = float(input('Type your weight:'))
hei = float(input('Type your height:'))
imc = wei / (hei**2)
if imc < 18.5:
    print('You are underweight!\nIMC:{:.1f}'.format(imc))
elif 18.5 <= imc <= 25:
    print('You are at the ideal weight!\nIMC:{:.1f}'.format(imc))
elif 25 < imc <= 30:
    print('You are overweight!\nIMC:{:.1f}'.format(imc))
elif 30 < imc <= 40:
    print('You are obese!\nIMC:{:.1f}'.format(imc))
else:
    print('You are morbidly obese!\nIMC:{:.1f}'.format(imc))

