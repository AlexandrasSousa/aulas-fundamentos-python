from operator import truediv

num1 = int(input("Digite um número"))
num2 = int(input("Digite outro número"))
num3 = int(input("Digite mas um número"))

while True:
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")
    opcao = int(input('Digite uma opção---> '))

    if opcao == 1:
      print (f"{num1} + {num2} +{num3}")

    elif opcao == 2:
        print (f"{num1}*{num2} *{num3}")

    elif opcao == 3:
       if num1>num2 and num1>num3:
           print(f"{num1} é o maior valor")
       elif num2>num1 and num2>num3:
           print(f"{num2} é o maior valor")
       elif num3 > num1 and num3 > num1:
           print(f"{num3} é o maior valor")

    elif opcao==5:
        print("Saindo")
    else:
        print("Opção inválida")