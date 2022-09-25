# Desenvolva um programa que leia o primeiro
# termo e a razão de uma PA. No final, mostre
# os 10 primeiros termos dessa progressão.
f1 = int(input('First term:'))
s2 = int(input('Second term:'))
t3 = f1 + (10 - 1) * s2
for c in range(f1, t3+s2, s2):
    print(c, end=' > ')
print('end!')
