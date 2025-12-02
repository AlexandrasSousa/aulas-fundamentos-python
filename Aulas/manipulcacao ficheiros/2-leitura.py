from pathlib import Path
caminho = Path (r"ficheiros/teste.txt")
with caminho.open(mode="r",encoding="utf-8", errors= "ignore") as file:
    for linha in file:
        print(linha, end="")