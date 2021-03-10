# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
erro = 1
while erro == 1:
    altura = float(input("Digite sua altura(Use . para valores decimais): "))
    sexo = input("Insira seu sexo(M OU F): ")

    if sexo == "M" or sexo == "m":
        peso_homem = 72.7*altura - 58
        if peso_homem.is_integer():
            peso_homem = int(peso_homem)
        print("Seu peso ideal é:", f'{peso_homem}KG')
        erro = 0

    elif sexo == "F" or sexo == "f":
        peso_mulher = 62.1*altura - 44.7
        if peso_mulher.is_integer():
            peso_mulher = int(peso_mulher)
        print("Seu peso ideal é:", f'{peso_mulher}KG')
        erro = 0

    else:
        print("Insira M ou F apenas")
        erro = 1

