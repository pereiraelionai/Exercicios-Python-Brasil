populacao_a = 80000
populacao_b = 200000
anos = 0

while True:
    populacao_a += populacao_a * 0.03
    populacao_b += populacao_b * 0.015
    print(f'População A: {populacao_a:.2f}\nPopulação B: {populacao_b:.2f}')
    print('------------------------------------')
    anos += 1
    if populacao_a > populacao_b:
        break
print(f'Será necessário {anos} anos para a população A ultrapassar a população B.')
