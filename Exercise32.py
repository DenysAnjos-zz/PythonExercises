# Faça um programa que leia um ano
# qualquer e mostre se ele é bissexto
from datetime import date
year = int(input('Type a year:'))
if year == 0:
    year = date.today().year
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('Its a leap year')
else:
    print('Its not a leap year')
