pessoas= []
qtd_pessoas = 0
soma_idade = 0
qtd_mulheres = 0
while True:
    dados = dict()
    dados["nome"]= input("Digite um nome:").strip()
    while True:
        dados ["sexo"] = input("digite o sexo [m/f]").strip().lower()
        if dados ["sexo"] != "m" and dados ["sexo"] != "f":
            print("por favor introduza um sexo válido:")
        else:
            break
    dados["idade"] = int(input("digite a idade:"))
    soma_idade=
    pessoas.append(dados)
    dados.clear()
    opcao= input("digite sim para terminar")
    if opcao == "sim":
        break
