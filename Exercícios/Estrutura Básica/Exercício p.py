# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total.

area = float(input("Informe apenas o valor numérico da área a ser pintada: "))

litro = area/3

lata = litro/18
if lata < 1:
    lata = 1
lata = float(lata) # Transformei em float para não dar problema com o .is_integer abaixo

if lata.is_integer():
    lata = int(lata)
else:
    lata = int(lata +1)

preco = lata * 80

if lata == 1:
    print(f'A quantidade de latas de tinta compredas é de: {lata} lata')
    print(f'O valor gasto é de: {preco}R$')

else:
    print(f'A quantidade de latas de tinta compredas é de: {lata} latas')
    print(f'O valor gasto é de: {preco}R$')
