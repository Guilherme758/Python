# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Informe a temperatura em graus fahrenheit: "))
celsius = 5 * (fahrenheit-32)/9

if celsius.is_integer() == True:
    celsius = int(celsius)

print("A temperatura em celsius é:", f'{celsius}ºC')
