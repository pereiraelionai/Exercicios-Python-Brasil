salario = float(input('Digite o seu salário: '))
novo_salario = 0
valor_aumento = 0
percentual = 0

if salario <= 280:
    percentual = 20/100
    valor_aumento = salario * percentual
    novo_salario = salario + valor_aumento
elif 280 < salario <= 700:
    percentual = 15/100
    valor_aumento = salario * percentual
    novo_salario = salario + valor_aumento
elif 700 < salario <= 1500:
    percentual = 10/100
    valor_aumento = salario * percentual
    novo_salario = salario + valor_aumento
else:
    percentual = 5/100
    valor_aumento = salario * percentual
    novo_salario = salario + valor_aumento

print(f'Seu salário atual é de R${salario:.2f}, portanto seu aumento será de R${valor_aumento:.2f} ({percentual * 100}%)'
      f' e seu novo salário será de R${novo_salario}.')
