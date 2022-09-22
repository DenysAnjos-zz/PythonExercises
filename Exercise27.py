# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# primário = Ana
# secundario = Maria
fullName = str(input('Type your full name:')).strip()
name = fullName.split()
print('Primary:', name[0])
print('Last:', name[len(name)-1])
