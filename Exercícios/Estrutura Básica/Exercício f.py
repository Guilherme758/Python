# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Informe o raio do círculo: '))
medida = input('A medida será em cm ou m?: ')

if medida != 'cm' and medida != 'm':
    print('Esse programa aceita apenas cm ou m. Tente novamente com uma dessas medidas')

else:
    print('Valor da área sendo π = 3:', f'{raio**2*3}{medida}²')
    print('Valor da área sendo π = 3,14:', f'{raio**2*3.14}{medida}²')