# Escreva um programa que pergunte o salário de um
# funcionário e calcule o valor do seu aumento.Para
# salários superiores a R$1250 calcule um aumento de
# 10% .Para os inferiores ou iguais o aumento é de 15%
salary = float(input('Type your salary:'))
if salary > 1250:
    print('New salary:', (salary + (salary * (10 / 100))))
else:
    print('New salary:', (salary + (salary * (15 / 100))))
