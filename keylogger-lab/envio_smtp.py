import smtplib
from email.message import EmailMessage
from pathlib import Path

# Configuração do laboratório
SERVIDOR = "127.0.0.1"
PORTA = 8025

REMETENTE = "simulador@laboratorio.test"
DESTINATARIO = "destinatario@laboratorio.test"

# Arquivo com os dados fictícios
arquivo = Path(__file__).resolve().parent / "registro_teclas.txt"

if not arquivo.is_file():
    print("Erro: arquivo de registros não encontrado.")
    raise SystemExit(1)

# Preparar a mensagem
mensagem = EmailMessage()
mensagem["From"] = REMETENTE
mensagem["To"] = DESTINATARIO
mensagem["Subject"] = "Laboratório - Registros simulados"
mensagem.set_content(
    "Registros fictícios do experimento:\n\n"
    + arquivo.read_text(encoding="utf-8")
)

# Enviar para o servidor SMTP local
try:
    with smtplib.SMTP(SERVIDOR, PORTA, timeout=10) as smtp:
        smtp.send_message(mensagem)

    print("Mensagem enviada ao servidor SMTP local.")

except (OSError, smtplib.SMTPException) as erro:
    print(f"Falha no envio: {erro}")
