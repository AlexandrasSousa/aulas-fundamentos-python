frase = input('Digite um frase: ').replace(' ', '').lower()

frase_reverse = ''

tam = len(frase)

for c in range(tam, 0, -1):
    frase_reverse += frase[c-1]

if frase_reverse == frase:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')