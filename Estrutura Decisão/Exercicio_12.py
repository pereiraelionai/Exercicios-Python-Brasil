valor_hora = float(input('Digite o valor da hora trabalhada: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas

ir = 0
ir_taxa = 0
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir_taxa = 5
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir_taxa = 10
    ir = salario_bruto * 0.1
else:
    ir_taxa = 20
    ir = salario_bruto * 0.2

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salario bruto: R${salario_bruto}')
print(f'(-) I.R ({ir_taxa}%): R${ir}')
print(f'(-) INSS: {inss}')
print(f'FGTS: R${fgts}')
print(f'Sindicato (3%): R${sindicato}')
print(f'Total de descontos: R${ir+inss+sindicato}')
print(f'Salário liquido: R${salario_liquido}')
