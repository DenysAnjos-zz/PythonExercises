# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre
# uma listagem de preços, organizando
# os dados em forma tabular.
products = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso',
            9.99, 'Mochila', 120.32,
            'Canetas', 22.30, 'Livro', 34.90)
a = 0
o = ''
for n in products:
    if a % 2 == 0:
        print(f'{n:.<30}{o}', end='')
    else:
        print(f'R${n:>7.2f}')
    a += 1

