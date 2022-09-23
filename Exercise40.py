# Crie um programa que leia duas notas de um
# aluno e calcule sua média, mostrando uma
# mensagem no final de acordo com a média atingida
# Média abaixo de 5.0: reprovado
# Média entre 5.0 e 6.9: recuperação
# Média 7.0 ou superior: aprovado
fi = float(input('Type your first grade:'))
se = float(input('Type your second grade:'))
media = (fi + se) / 2
if media < 5.0:
    print('Disaproved!')
elif media >= 7.0:
    print('Approved!')
else:
    print('Recovery!')

