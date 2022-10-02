# Crie um programa que leia uma frase
# qualquer e diga se ela é um palindromo
# , desconsiderando os espaços.
text = input('Type a palindrome:').strip().upper()
words = text.split()
tog = ''.join(words)
inv = ''
for letter in range(len(tog)-1, -1, -1):
    inv += tog[letter]
if inv == tog:
     print('We have a palindrome!')
else:
     print('We dont have a palindrome!')
