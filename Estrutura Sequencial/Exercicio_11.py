num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite um número inteiro: '))
num_real = float(input('Digite um número: '))

a = (num_1 * 2) + (num_2 / 2)
b = (num_1 * 3) + num_real
c = num_real ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevado ao cubo: {c}')
