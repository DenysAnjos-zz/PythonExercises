# Faça um programa que leia o ano de nascimento de um
# jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo
age = int(input('Type your age:'))
if age > 18:
    print('It past time to enlist:{} years'.format(age))
elif age == 18:
    print("It's time to enlist")
else:
    print('Still {} years to enlist'.format(age))
    