nota_1 = int(input('Digite a primeira nota:'))
nota_2= int(input("Digite a segunda nota"))
nota_3= int(input("Digite a terceira nota"))
nota_4= int(input("Digite a quarta nota"))
nota_5= int(input("Digite a quinta nota"))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

nota_final = media

if nota_final >=9.5:
    print("Parabéns, você passou!")
elif nota_final  <= 9.5:
    print("Opa, você está de recuperação!")
elif nota_final < 8:
    print(" você está reprovado!!")

print("sua nota final é:", nota_final)