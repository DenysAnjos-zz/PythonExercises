# Crie um programa onde o usuário digite uma
# expressão qualquer que use parênteses. Seu
# aolicativo deverá analisar se a expressão
# passada está com os parênteses abertos
# e fechados na ordem correta.
expr = str(input('Type a math expression:'))
test = list()
for c in expr:
    if c == '(':
        test.append('(')
    elif c == ')':
        if len(test) > 0:
            test.pop()
if len(test) == 0:
    print('Correct!')
else:
    print('Error!')




