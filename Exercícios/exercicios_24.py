limite_velocidade = 80

print("----RADAR DE VELOCIDADE----")
velocidade = int(input("----»"))
if velocidade > limite_velocidade:
    print("MULTADO!!!")
    multa = 100
    custo_km = 7

    valor_multa = multa + custo_km * (velocidade - limite_velocidade)
    print(" O total a pagar é:", valor_multa ,"€")


elif velocidade <= velocidade:
    print("NÃO MULTADO!!!")

print("Boa Viagem")

