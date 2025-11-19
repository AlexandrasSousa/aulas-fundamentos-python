resposta = " "
print("o céu é azul?")
while resposta!= "V" and resposta !="F":
    resposta = input("[V/F]:").strip().upper()
    if resposta == "V":
        print("Acertou")
    elif resposta == "F":
        print ("Errou")
    else:
        print("resposta inválida")

print("o palmeiras tem mundial?")
while True:
    resposta = input("[V/F]:").strip().upper()
    if resposta == "V":
        print("errou")
    elif resposta == "F":
        print ("acertou vamos a proxima")
    else:
        print("resposta inválida")

    print("o formador é o ricardo?")
while True:
    resposta = input("[V/F]:").strip().upper()
    if resposta == "V":
        print("Acertou, fim")

    elif resposta == "F":
        print ("Errou")

    else:
        print("resposta inválida")
