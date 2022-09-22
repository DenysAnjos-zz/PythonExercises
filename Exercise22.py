# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas
# > O nome com todas as letras minúsculas
# > Quantas letras ao todu(sem considerar espaço
# > Quantas letras tem o primeiro nome
name = str(input('Type your full name:')).strip()
print('Capital Leters', name.upper())
print('Lowercase:', name.lower())
print('Total letters:', len(name)-name.count(' '))
print('First name letters: ', name.find(' '))



