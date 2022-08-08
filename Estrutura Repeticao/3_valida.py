while True:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    salario = float(input('Digite o seu salario: '))
    sexo = input('Digite seu sexo [M/F]: ').upper()
    estado_civil = input('Digite seu estado civil[S, C, V, D]: ').upper()

    if len(nome) < 3:
        print('O nome deve conter no mínimo 3 caracteres.')
        continue

    if not 0 < idade < 150:
        print('A idade deve ser entre 0 e 150 anos.')
        continue

    if not salario > 0:
        print('O salário deve ser maior que R$ 0,00')
        continue

    if sexo not in 'FM':
        print('O sexo deve ser Masculino[M] ou Feminino[F]')
        continue

    if estado_civil not in 'SCVD':
        print('O sexo deve ser S, C, V, D')
        continue
    break
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salario: {salario}')
print('Masculino' if sexo == 'M' else 'Feminino')
print(f'Estado civil: {estado_civil}')
