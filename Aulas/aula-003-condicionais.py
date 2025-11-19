limite_velocidade = 120
minimo_vlocidade = 50
print("----RADAR DE VELOCIDADE----")
velocidade = int(input("----»"))
if velocidade > limite_velocidade:
    print("MULTADO!!!")
elif velocidade < minimo_vlocidade:
    print("ACELERA UM POUCO!")
else:
    print("BOA VIAGEM!")

print("Fim do Programa")