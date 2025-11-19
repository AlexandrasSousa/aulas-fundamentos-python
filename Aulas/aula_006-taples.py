#estante = "xbox", "plastation", "nitendo", "gameboy"
#print (estante[0])

#estante = input("Digite uma console:"),input ("Digite uma console:"),input ("Digite uma console:"), input ("Digite uma console:")
#print (estante[3])


nomes = ("nadia", "julia","alexandra", "telmo", "victor","rafael",
        "daniel","leticia", "roman", "pedro", "francisco", "ines")

print (nomes)
tam = len (nomes)
print(tam)
for c in range ( 0, len (nomes)):
    print(f"{c} -» {nomes [c]}")
for nome in nomes:
    print(nome)
for indice, nome in enumerate (nomes):
    print(f"no indice {indice } e valor é {nome} ")
print (sorted(nome))

