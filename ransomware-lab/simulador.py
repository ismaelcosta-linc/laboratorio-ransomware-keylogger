
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent

ORIGEM = BASE / "arquivos_teste"
DESTINO = BASE / "copias_teste"
CRIPTOGRAFADOS = BASE / "criptografados"
RECUPERADOS = BASE / "recuperados"

# Chave didatica para transformacao XOR
CHAVE = b"LAB2026"


def transformar(dados):
    return bytes(
        valor ^ CHAVE[i % len(CHAVE)]
        for i, valor in enumerate(dados)
    )


def preparar_arquivos():
    DESTINO.mkdir(exist_ok=True)

    for arquivo in ORIGEM.glob("*.txt"):
        shutil.copy2(arquivo, DESTINO / arquivo.name)
        print(f"Copia criada: {arquivo.name}")


def criptografar_copias():
    CRIPTOGRAFADOS.mkdir(exist_ok=True)

    for arquivo in DESTINO.glob("*.txt"):
        dados = arquivo.read_bytes()
        resultado = transformar(dados)

        saida = CRIPTOGRAFADOS / (arquivo.name + ".simulado")
        saida.write_bytes(resultado)

        print(f"Arquivo transformado: {saida.name}")


def criar_nota_resgate():
    modelo = BASE / "modelo-nota-resgate.txt"
    destino = CRIPTOGRAFADOS / "LEIA-ME.txt"

    shutil.copy2(modelo, destino)
    print(f"Nota de resgate simulada criada: {destino.name}")


def recuperar_arquivos():
    RECUPERADOS.mkdir(exist_ok=True)

    for arquivo in CRIPTOGRAFADOS.glob("*.simulado"):
        dados = arquivo.read_bytes()
        resultado = transformar(dados)

        nome_original = arquivo.name.removesuffix(".simulado")
        saida = RECUPERADOS / nome_original

        saida.write_bytes(resultado)
        print(f"Arquivo recuperado: {saida.name}")


if __name__ == "__main__":
    preparar_arquivos()
    criptografar_copias()
    criar_nota_resgate()
    recuperar_arquivos()
    print("Simulacao concluida.")

