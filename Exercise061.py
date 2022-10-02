# Refaça o desafio 051, lendo o primeiro termo e
# a razão de uma pa, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
f1 = int(input('First term:'))
s2 = int(input('Second term:'))
n = 0
while n != 10:
    print(f1, end=' > ')
    f1 = s2 + f1
    n += 1
print('end!')