# 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
# seu novo salário, com 15% de aumento.
salary = float(input('Type your salary:R$'))
print('Your new salary is R${:.2f}'.format(salary+(salary*(15/100))))
