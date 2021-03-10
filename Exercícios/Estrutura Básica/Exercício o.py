# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o
# salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato (5%) : R$
# = Salário Liquido : R$

valor_hora = float(input("Por hora, quantos R$ você ganha?: "))
horas = float(input('No mês, quantas horas você trabalhou?: '))

bruto = valor_hora * horas

ir = bruto * 0.11
if ir.is_integer():
    ir = int(ir)

inss = bruto * 0.08
if inss.is_integer():
    inss = int(inss)

sindicato = bruto * 0.05
if sindicato.is_integer():
    sindicato = int(sindicato)

liquido = bruto - (ir + inss + sindicato)
if liquido.is_integer():
    liquido = int(liquido)

if bruto.is_integer():
    bruto = int(bruto)
    # Em alguns casos bruto será inteiro, porém inteiro não tem o atributo .is_integer, logo se sua
    # conversão de int ficar acima, todas as outras variáveis também serão inteiras, por isso
    # coloquei sua conversão no final

print(f'Seu salário bruto é: {bruto}R$')
print(f'O valor pago ao Imposto de Renda(IR) é de: {ir}R$')
print(f'O valor pago ao Instituto Nacional do Seguro Social(INSS) é de: {inss}R$')
print(f'O valor pago ao Sindicato é de: {sindicato}R$')
print(f'Seu salário líquido é: {liquido}R$')
