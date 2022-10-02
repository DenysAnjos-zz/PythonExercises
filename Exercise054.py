# Crie um programa que leia o ano de nascimento
# de sete pessoas. No final mostre quantas
# pessoas ainda não atingiram a maioridade
# e quantas são maiores
from datetime import date
over, under = 0, 0
today = date.today().year
for c in range(0, 7):
    check = int(input('Type your birth:'))
    age = (today - check)

    if age >= 21:
        over += 1
    else:
        under += 1
print(over, 'people have reached the age of majority.')
print(under, 'people have not reached the age of majority.')
