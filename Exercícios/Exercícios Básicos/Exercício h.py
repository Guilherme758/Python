# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.

valor = float(input('Quanto vale uma hora de trabalho sua? (Use . para se referir a valores decimais): '))
horas = int(input('Quantas horas você trabalhou no mês?: '))
mes = valor*horas

if mes.is_integer() == True:
    mes = int(mes)

print("O valor que você deve ganhar no mês é de:", mes)
