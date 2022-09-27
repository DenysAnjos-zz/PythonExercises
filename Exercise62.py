# Melhore o desafio 61, perguntando para o
# usário se ele quer mostrar mais alguns
# termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.
f1 = int(input('First term:'))
s2 = int(input('Second term:'))
n = 0
while n != 10:
    print(f1, end=' > ')
    f1 = s2 + f1
    n += 1
    if n == 10:
        print('STOP!')
        check = int(input('Type 0 for stop:'))
        if check != 0:
            n = 0
            f1 = int(input('First term:'))
            s2 = int(input('Second term:'))
print('END!')
