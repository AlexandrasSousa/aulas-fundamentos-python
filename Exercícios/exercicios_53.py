
from random import randint
numeros_aleatorios = randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10)
for c in range (0, len (numeros_aleatorios)):
    print(numeros_aleatorios)
    break
maior_num = menor_num = numeros_aleatorios[0]

for num in numeros_aleatorios:
    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num
print(f"Menor número aleatório: {menor_num}")
print(f"Maior número aleatórioo: {maior_num}")
