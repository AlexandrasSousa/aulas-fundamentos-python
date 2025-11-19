num_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte")

numero = int(input("Digite um número entre 0 e 20: "))
while True :
    if 0 <= numero <= 20:
        print(f"{numero} -> {num_extenso[numero]}")
        break
    else:
        print("Número número inválido.")
        break

