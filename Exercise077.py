# Crie um programa que tenha uma tupla
# com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais
words = ('Erik', 'chupa', 'pau', 'mole')
for w in words:
    print(f'\nIn {w} we have:', end=' ')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
