nome = input("Digite seu nome:").strip()
print(nome.upper())  #todas letras maiusculas
print(nome.lower()) #minusculas
print(len(nome.replace(' ', ''))) #quantidade de letras sem espaço
pEspaco = nome.find(' ')
print(nome[:pEspaco])
