num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

if num1 > num2 and num1 > num3:
    primeiro = num1
elif num2 > num3:
    primeiro = num2
else:
    primeiro = num3

if num1 < num2 and num1 < num3:
    terceiro = num1
elif num2 < num3:
    terceiro = num2
else:
    terceiro = num3

if num2 < num1 < num3 or num2 > num1 > num3:
    segundo = num1
elif num1 < num2 < num3 or num1 > num2 > num3:
    segundo = num2
elif num1 < num3 < num2 or num1 > num3 > num2:
    segundo = num3

print(primeiro, segundo, terceiro)
