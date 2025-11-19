caracter = "*"
espaco = " "
quant_espaco = 5
print("---Desenhador de Formas---")
print("[1] Escada direita")
print("[2] Escada esquerda")
print("[3] Triângulo")
print("[4] Letra X")

opcao = int(input("Escolha uma das opções: "))

if opcao == 1:
    # Escada à direita (1 a 5 asteriscos)
    for c in range(1, quant_espaco + 1):
        print(caracter * c)

elif opcao == 2:
    # Escada à esquerda (alinhada à direita)
    for c in range(1, quant_espaco + 1):
        num_caracteres = c
        num_espacos = quant_espaco - num_caracteres
        print((espaco * num_espacos) + (caracter * num_caracteres))

elif opcao == 3:
    # Triângulo centralizado (altura = quant_espaco)
    altura = quant_espaco
    for c in range(altura):
        num_caracteres = 2 * c + 1  # 1, 3, 5, ...
        num_espacos = altura - c - 1  # espaços à esquerda para centralizar
        print((espaco * num_espacos) + (caracter * num_caracteres))

elif opcao == 4:
    caracter = "*"
    espaco = " "
    tamanho = 5  # deve ser ímpar para ficar simétrico
    for i in range(tamanho):
        # posição inversa da segunda diagonal
        j = tamanho - 1 - i

        linha = ""
        for k in range(tamanho):
            if k == i or k == j:
                linha += caracter
            else:
                linha += espaco
        print(linha)



