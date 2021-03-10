# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

num1 = float(input("Digite um número inteiro: "))
if num1.is_integer() == False:
    print("Por favor, digite um número inteiro")

num2 = float(input("Digite outro número inteiro: "))
if num2.is_integer() == False:
    print('Por favor, digite um número inteiro')

num3 = float(input("Digite um número real(número decimal de preferência): "))

# A
a = (num1*2) * (num2/2)
print("Produto do dobro do primeiro número com o segundo:", a)

# B
b = (num1*3) + num3
print("Soma do triplo do primeiro número com o terceiro:", b)

# C
c = num3**3
print("Terceiro número elevado ao cubo:", c)
