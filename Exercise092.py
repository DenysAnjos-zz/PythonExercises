# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de
# ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além
# da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
person = dict()
person['name'] = str(input('Name:'))
birth = int(input('Year birth:'))
age = (datetime.now().year - birth)
person['workC'] = int(input('Work card(0 if you dont have):'))
if person['workC'] != 0:
    person['yearH'] = int(input(f'Year of hire:'))
    person['salary'] = float(input(f'Salary:'))
    person['retirement'] = (age + (person["yearH"] + 30) - datetime.now().year)
print('-=' * 20)
for i, v in person.items():
    print(f'{i} has the value {v}')
    