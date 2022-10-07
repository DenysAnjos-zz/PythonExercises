# Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre
# qual foi o maior e o menor valor digitado e
# as suas respectivas posições na lista.
valores = list()
for count in range(0, 5):
    valores.append(int(input('Digite um valor:')))
biggest = smaller = posBig = posSmal = 0
for c, v in enumerate(valores):
    if smaller == 0:
        smaller = v
    if smaller > v:
        smaller = v
        posSmal = c
    if biggest < v:
        biggest = v
        posBig = c

print(f'The biggest is {biggest} and its position is {posBig}.')
print(f'The smaller is {smaller} and its position is {posSmal}.')
