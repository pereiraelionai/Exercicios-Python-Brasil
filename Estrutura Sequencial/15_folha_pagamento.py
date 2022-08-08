valor_hora = float(input('Digite o salario por hora: '))
horas_mes = float(input('Digite as horas trabalhadas por mês: '))

salario_bruto = valor_hora * horas_mes

importo = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
descontos = importo + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f'+ Salario Bruto: {salario_bruto}')
print(f'- Imposto de renda: {importo}')
print(f'- INSS: {inss}')
print(f'- Sindicato: {sindicato}')
print(f'= Salariom liquido: {salario_liquido}')
