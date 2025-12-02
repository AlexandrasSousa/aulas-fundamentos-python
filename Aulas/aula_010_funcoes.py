def cabecalho(txt):
    print("-"*20)
    print(f"{txt:-^20}")

def soma ("soma"):
    num1 = int(input( "digite um numero"))
    num2 = int(input("digite outro numero"))
    print(f"{num1}+{num2} ={num1}+{num2}")
def menu():
    cabecalho("Menu")
    print("[1]- soma")
    print("[2]- subtração")
    print("[3]- multiplicação")
    print("[4]- divisão")
    print("-" * 20)
    if opcao ==1:
        soma()