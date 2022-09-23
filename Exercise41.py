# A confederação nacional de natação precisa
# de um programa que leia o ano de
# nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 25 anos: senior
# Acima: master
from datetime import date
birth = int(input('Type your year of birth:'))
age = date.today().year - birth
if age <= 9:
    print('You are: Mirim!')
elif age <= 14:
    print('You are: Infantil!')
elif age <= 19:
    print('You are: Junior!')
elif age <= 25:
    print('You are: Senior!')
else:
    print('You are: Master!')
