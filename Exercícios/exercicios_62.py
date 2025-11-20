numeros = list()

for linha in range (0,3):
    temp = list()
    soma_valores_pares = 0
    soma_segunda_coluna = 0
    maior_terceira_linha = ""

    for coluna in range(0,3):
        num = int(input( "digite um número:"))
        if num %2==0:
            soma_valores_pares += num
        if coluna ==1:
            soma_segunda_coluna += num
        if linha ==2:
            if coluna == 0:
                maior_terceira_linha = num
            else:
                if num > maior_terceira_linha:
                    maior_terceira_linha = num
        temp.append(num)
    numeros.append(temp[:])
print(numeros[0][2])
for lista in numeros:
    print (lista)
    for valor in lista:
        print(valor, end=" ")
    print()

    print(f"soma valores pares",  soma_valores_pares)
    print(f"soma valores segunda coluna", soma_segunda_coluna)
    print(f"maior valor da terceira linha", maior_terceira_linha)