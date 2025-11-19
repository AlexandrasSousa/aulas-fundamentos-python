campeonato_espanhol = ("Real Madrid", "Barcelona","Villarreal","Real Betis","Atlético de Madrid",
                       "Sevilla","Elche","Athletic Club","Espanyol", "Alavés","Getafe","Osasuna",
                       "Levante","Rayo Vallecano","Valencia", "Celta de Vigo", "Girona",
                       "Real Sociedad", "Mallorca")
for c in range (0,5, len (campeonato_espanhol)):
    print(f" Os 5 primeiros  classificados pelo campeonato espanhol foram: {campeonato_espanhol [c:5]}\n")
for c in range (0,5, len (campeonato_espanhol)):
    print(f" Os 4 ultimos  classificados pelo campeonato espanhol foram: {campeonato_espanhol [15:21]}\n")
    print(sorted(campeonato_espanhol ))

    print("posicao da esquipe las palmas:")
    esta_la = False
    indice_las_palmas = ""

    for indice, equipa in enumerate (campeonato_espanhol):
        if equipa == "las palmas":
            esta_la = True
            indice_las_palmas = indice
    if esta_la :
        print(f" las palma _»{indice_las_palmas +1}º lugar")
    else:
        print("Las palmas não está classificado")
