# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. no final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
nameGrade = list()
all = list()
while True:
    name = str(input('Type your name:'))
    nameGrade.append(name)
    note = int(input('Type your grade:'))
    nameGrade.append(note)
    all.append(nameGrade[:])
    check = str(input('Do you want continue?(y/n) '))
    if check == 'nN':
        break