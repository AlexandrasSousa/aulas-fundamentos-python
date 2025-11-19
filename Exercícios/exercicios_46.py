soma = 0
contador = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break

    soma += numero
    contador += 1

print(f'A soma entre os valores digitados é: {soma}.')
print(f'Digitou {contador} números.')