# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Passe a temperatura em celsius: '))
fahrenheit = 9*(celsius/5)+32

if fahrenheit.is_integer() == True:
    fahrenheit = int(fahrenheit)

print("A temperatura em fahrenheit é:", f'{fahrenheit}ºF')