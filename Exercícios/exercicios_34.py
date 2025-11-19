qtd_pares =0
for c in range (0,10):
    numero = int(input(f" Digite o {c + 1}º número: "))

    if numero %2 == 0:
        print("Esse número é: Par!")
        qtd_pares += 1
print(f" {qtd_pares} numeros digitados são pares")