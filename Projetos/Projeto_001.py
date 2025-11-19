print("--- Calculadora IMC---")

altura = float(input("Digite sua altura"))
peso = float(input("Digite seu Peso"))
imc =  peso / (altura *altura)
print(f'Seu indice de massa corporal é: {imc:.2f}')
if imc ==  18.5 or 24.9:
    print("Peso normal")

elif imc == 25.0 or 29.9:
    print("sobrepeso")

elif imc == 30 or 34.9:
    print("Obesidade grau 1")

elif imc == 35.0 or 39.9:
    print("Obesidade grau 2")

elif imc >= 40.0 or 39.9:
    print("Obesidade grau 3")
    print("Obesidade morbida")

