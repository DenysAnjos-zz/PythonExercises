# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "a"
# > Em que posição ela aparece a primeira vez
# > Em que posição ela apareceu a ultima vez.
text = str(input('Type a text:')).upper().strip()
print('Letter "A" appears:', text.count('A'))
print('First position:', (text.find('A')+1))
print('Last position:', (text.rfind('A')+1))
