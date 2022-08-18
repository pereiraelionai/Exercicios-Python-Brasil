size_file = float(input('Digite o tamanho do arquivo em MB: '))
internet_speedy = float(input('Digite a velocidade da internet em Mbps: '))
internet_speedy_bits = internet_speedy / 8

download_time = size_file / internet_speedy_bits
print(f'O download será consluído em {download_time:.0f} segundos')
