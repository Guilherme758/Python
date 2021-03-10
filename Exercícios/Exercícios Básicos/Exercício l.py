# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura(Use . para valor decimal): "))
peso_ideal = 72.7*altura - 58

if peso_ideal.is_integer():
    peso_ideal = int(peso_ideal)

print("Seu peso ideal é:", f'{peso_ideal}KG')
