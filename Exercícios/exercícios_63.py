#crie um programa que crie palpites para euromilhoes. O programa deve perguntar
#quantas chaves serão gerada e deve sortear aletoriamente 5 numeros de 1 a 5 (sem repetir)
# e 2 estrellas de 1 a 12 (sem repetir). cada sorteio deve ser quardado numa lista.


import random
from time sleep
print("---Gerador euromilhões---")



n_palpites = int(input("Quantos palpites deseja gerar"))
sleep(1)
print(f"a gerar {n_palpites}")
for c in range (n_palpites):

    numeros = []
    estrelas = []
    palpites = []
    while len(numeros) < 5:
        numeros = random.randint(1, 50)
        if  numeros not in numeros:
            numeros.append (numeros)
    while len (estrelas)<2:
        estrelas = random.randint(1, 12)
        if  estrelas not in estrelas:
            estrelas.append (estrelas)
palpites.append(sorted(numeros[:]))
numeros.append(sorted(estrelas[:]))

for indice, linha in enumerate (palpites):
    if indice == 0:
        for numero in linha:
         print(f"{numero} |", end = "")
    else indice ==
        estrelas in linha:
        print(f"*{estrelas} |", end="")