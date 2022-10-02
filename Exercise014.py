# Escreva um programa que converta uma temperatura digitada em C
# para F #
celsius = float(input('Whats the temperature in C°?'))
fahrenheit = ((9 * celsius) / 5) + 32
print('{:.1f}C° in fahrenheit is:{:.1f}°F' .format(celsius, fahrenheit))
