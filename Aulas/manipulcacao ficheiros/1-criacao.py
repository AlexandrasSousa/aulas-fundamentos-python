from pathlib import Path
caminho = Path (r"ficheiros/teste.txt")
print("caminho criado com sucesso")
with caminho.open("w", encoding="utf-8", errors= "ignore") as file:
    print("ficheiro aberdo em modo escrita com sucesso")
    file.write("Olá turma\n")
    file.write("Olá novamente")
    print("mensagens escritas com sucesso")