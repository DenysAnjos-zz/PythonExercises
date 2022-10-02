# Faça um programa que leia o sexo de uma
# pessoa, mas só aceite os valores 'M' ou
# 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.
check = input('Type your sex:').lower()
while check != 'm' and check != 'w':
    print('Invalid data, try again!')
    check = input('Type your sex:').lower()
print('Registered data!')
