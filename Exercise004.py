# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possiveis sobre ele
n = input('Type something:')
print(n)
print('Type?', type(n))
print('Only space??', n.isspace())
print('Decimal?]?', n.isdecimal())
print('Numeric??', n.isnumeric())
print('Alphabetic?', n.isalpha())
print('Alphanumeric??', n.isalnum())
print('All uppercase??', n.isupper())
print('Capitalized?', n.istitle())

