from random import randint

num_aleatorio = randint(1, 10)
tentativas =0
num=-1
print("---JOGO DO ADIVINHA 2.0---")
print ("Adivinhe um número entre 1 e 1O:")
print (num_aleatorio)
while num!= num_aleatorio:
    num = int(input("Digite um número:"))
    tentativas +=1

    if num < num_aleatorio:
        print ("Opa, o número é maior!")
    elif num == num_aleatorio:
        print(f"Você acertou!! eu pensei no {num_aleatorio}")
        print(f"total de tentativas:{tentativas}")
    elif num > num_aleatorio:
     print("Opa, o número é menor!!")
