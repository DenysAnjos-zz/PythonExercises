# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo
for c in range(0, 10):
   n = int(input('Type a number:'))
   if n != 2 and n != 3 or n % 2 == 0 or n % 3 == 0:
       print(n, " is a prime number!")

   else:
       print(n, ' is not a prime number!')