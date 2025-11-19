from time import sleep
print("****Registro de utilizador****")
nome = input("nome:")
sleep(1)
print( f"Olá {nome}, o seu registro esta completo")

sleep(0.5)
print("A gerar o seu email...")
sleep(1)

p_nome =nome [0]
indice_espaco = nome.find(' ') +1
u_nome = nome [indice_espaco:]
email = f"{p_nome}.{nome}""@empresa.pt"
print ("seu emeil é", email)