maior_num = 0

for n in range(5):
    num = int(input('Digite um número: '))
    if num > maior_num:
        maior_num = num
print(f'O maior número é: {maior_num}')
