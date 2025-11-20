numeros = list()
for linha in range (0,3):
    temp = list()

    for coluna in range(0,3):
        num = int(input( "digite um número:"))
        temp.append(num)
    numeros.append(temp[:])
print(numeros[0][2])
for lista in numeros:
    print (lista)
    for valor in lista:
        print(valor, end=" ")
    print()