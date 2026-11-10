from datetime import datetime
from pathlib import Path

arquivo = Path(__file__).resolve().parent / "registro_teclas.txt"

print("=== Simulador educacional de Keylogger ===")
print("Digite apenas informações fictícias.")
print("Digite SAIR para encerrar.\n")

with arquivo.open("a", encoding="utf-8") as registro:
    while True:
        texto = input("Entrada de teste: ")

        if texto.upper() == "SAIR":
            break

        horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro.write(f"[{horario}] {texto}\n")
        registro.flush()

print("\nSimulação encerrada.")
print(f"Registros armazenados em: {arquivo.resolve()}")

