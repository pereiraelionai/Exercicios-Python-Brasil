letra = input('Digite F(feminino) ou M(masculino): ').upper()
sexo = ''

if letra == 'F':
    sexo = 'Feminino'
elif letra == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Sexo inválido'

print(sexo)
