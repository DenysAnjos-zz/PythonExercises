# Faça um programa que leia o ano de nascimento de um
# jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo
from datetime import date
birth = int(input('Year of birth:'))
age = date.today().year - birth
if age > 18:
    print('You have:{} years, it past time to enlist:{} years'.format(age, age-18))
elif age == 18:
    print("You have:{} years, it's time to enlist".format(age))
else:
    print('You have:{} years, still {} years to enlist'.format(age, -age+18))
    