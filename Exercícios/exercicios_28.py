import random
print("---JOGO DO ADIVINHA---")
num_aleatorio = random.randint(1, 7)
num_1 = int(input("Digite um número:"))
print (num_aleatorio)
if num_1 == num_aleatorio:
    print("Você acertou!!")
else:
    print("Você errou!!")
