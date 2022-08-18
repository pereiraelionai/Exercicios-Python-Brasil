num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

if num1 >= num2 and num1 >= num3:
    print(f'Maior: {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'Maior: {num2}')
elif num3 >= num1 and num3 >= num2:
    print(f'Maior: {num3}')

if num1 <= num2 and num1 <= num3:
    print(f'Menor: {num1}')
elif num2 <= num1 and num2 <= num3:
    print(f'Menor: {num2}')
elif num3 <= num1 and num3 <= num2:
    print(f'Menor: {num3}')

if num1 == num2 == num3:
    print('Os números são iguais')
