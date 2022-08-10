sexo = input('Digite (h)-homem ou (m)-mulher: ').lower()
altura = float(input('Digite sua altura (m): '))
peso_ideal = 0

if sexo == 'h':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'm':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print('Selecione um sexo válido.')

if peso_ideal != 0:
    print(f'Seu peso ideal é: {peso_ideal:.2f}Kg')
