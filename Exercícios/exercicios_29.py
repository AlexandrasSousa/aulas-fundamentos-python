print('--- Calculadora ---')
print('[ 1 ] – Tabuada')
print('[ 2 ] – Calculadora')
print('[ 3 ] – Numeros pares')
print('[ 4 ] – Sair')
opcao = input('--> ')

if opcao == '1':
    print('Escolheu tabuada')
    numero = int(input("Digite um número:"))
    print(numero, "x 1=", numero * 1)
    print(numero, "x 1=", numero * 2)
    print(numero, "x 1=", numero * 3)
    print(numero, "x 1=", numero * 4)
    print(numero, "x 1=", numero * 5)
    print(numero, "x 1=", numero * 7)
    print(numero, "x 1=", numero * 8)
    print(numero, "x 1=", numero * 9)
    print(numero, "x 1=", numero * 10)

elif opcao == '2':
    print("Escolheu calculadora")
    num1 = int(input("Digite um número:"))
    num2 = int(input("Digite outro número:"))
    operacao = input(" +, -, *,/")
    if operacao == "+":
        print(num1+num2)
    elif operacao =="-":
        print(num1 - num2)
    elif operacao =="*":
        print(num1 * num2)
    elif operacao =="/":
        if num2 ==0:
            print("Não é possivel dividir por 0")
        else:
            print(num1 / num2)


elif opcao == "3":
    print("Numeros pares")
    num= input("Digite um número:")
    numero = int (num)
    if numero %2 == 0:
        print("Esse número é Par!")
    elif numero %2 != 0:
        print("Esse numero não é par")


elif opcao == "4":
    print('Você Saiu')



