## Trabalho grupo 4
# #Alexandra, Nadia, Leticia

print("Seja bem vindo ")
usarname = input("Digite seu nome")
email = input("Digite seu e-mail")
password = input("Digite a palavra passe")

print(usarname, "Seu registro foi feito com sucesso!")
print("[1] - Login ")
print("[2] - Sair")
opcao = input("Escolha uma opção")
if opcao == "1":
    print("Login")
    login = input("Digite seu e-mail")
    passe = input ("Digite sua palavra passe")
    if email == login and password == passe:
            print ("Login efetuado com sucesso")
    else:
        login = input("Digite  novamente seu e-mail")
        passe = input ("Digite novamente sua palavra passe")
        if email != login and password != passe:
            print("Sua conta foi bloqueada")

elif opcao == "2":
    print("Você saiu!")
