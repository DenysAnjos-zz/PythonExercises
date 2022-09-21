# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "a"
# > Em que posição ela aparece a primeira vez
# > Em que posição ela apareceu a ultima vez.
text = str(input('Type a text:'))
print('Letter "a" appears:', text.count('a'))
print('First position:', text.find('a'))
print('Last position:', text.rfind('a'))
