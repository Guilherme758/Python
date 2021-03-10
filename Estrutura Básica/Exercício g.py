# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

area = float(input('Informe o valor do lado do quadrado: '))
medida = input('a área será em cm ou m: ')

if medida != 'cm' and medida != 'm':
    print('Este programa utiliza apenas cm e m. Tente novamente com uma dessas medidas')

else:
    print('O dobro da área do quadrado é:', f'{(area*area)*2}{medida}²')