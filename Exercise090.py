# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No
# final, mostre o conteúdo da estrutura na tela.
student = {}
student['name'] = str(input('Name:'))
student['grade1'] = float(input('Grade 1:'))
student['grade2'] = float(input('Grade 2:'))
student['average'] = float(student['grade1'] + student['grade2']) / 2

print(f'Your name is {student["name"]}')
print(f'Your average is {student["average"]}')
if student['average'] >= 7:
    print('You are approved!!!')
else:
    print('You are in recovery.')
