# Laboratório de Cibersegurança — Simulação de Ransomware e Keylogger

## 1. Sobre o projeto

Projeto desenvolvido como atividade prática do curso de Cibersegurança Santander/DIO, com o objetivo de estudar o funcionamento de dois tipos de malware: ransomware e keylogger.

Os experimentos foram realizados em ambiente controlado, utilizando simulações desenvolvidas em Python, sem utilização de malware real ou comprometimento de sistemas de terceiros.

## 2. Ambiente e ferramentas

- Sistema operacional: Debian GNU/Linux 13.
- Linguagem de programação: Python 3.
- Ferramentas: terminal Linux, bibliotecas Python e servidor SMTP local.
- Apoio ao desenvolvimento e à documentação: chatbot do ChatGPT.

## 3. Laboratório de Ransomware

Diretório: `ransomware-lab/`

Foi desenvolvido um simulador de ransomware utilizando a operação XOR para realizar uma transformação reversível em arquivos fictícios.

O experimento incluiu:

- Criação de arquivos de teste.
- Transformação reversível dos arquivos.
- Geração automática de uma nota de resgate simulada (`LEIA-ME.txt`), com advertência sobre os riscos de pagar resgates.
- Recuperação dos arquivos originais.
- Verificação de integridade por meio de hashes SHA-256.
- Registro das evidências e dos resultados.

A simulação foi limitada aos arquivos preparados especificamente para o laboratório.

Mais detalhes: [README do Ransomware](ransomware-lab/README.md).

## 4. Laboratório de Keylogger

Diretório: `keylogger-lab/`

Foi desenvolvido um simulador de keylogger que utiliza entradas voluntárias e fictícias para demonstrar o registro e a transmissão de informações.

O experimento incluiu:

- Simulação de entradas de texto.
- Armazenamento dos registros em arquivos `.txt`.
- Transmissão dos registros para um servidor SMTP local (`127.0.0.1:8025`).
- Verificação do recebimento das mensagens.
- Registro das evidências e dos resultados.

Foram utilizados endereços de e-mail fictícios, sem envio de informações para serviços externos.

Mais detalhes: [README do Keylogger](keylogger-lab/README.md).

## 5. Medidas preventivas

Os experimentos permitiram compreender a importância de medidas de proteção, como:

- Manter cópias de segurança periódicas e isoladas.
- Atualizar o sistema operacional e os aplicativos.
- Evitar a execução de arquivos desconhecidos.
- Utilizar ferramentas de proteção contra malware.
- Aplicar o princípio do menor privilégio.
- Monitorar atividades suspeitas e conexões de rede.
- Utilizar regras de firewall para restringir comunicações não autorizadas.

## 6. Organização do projeto

```text
projeto-final/
├── ransomware-lab/
│   ├── simulador.py
│   ├── modelo-nota-resgate.txt
│   ├── mensagem-simulada.txt
│   ├── README.md
│   ├── arquivos_teste/
│   ├── copias_teste/
│   ├── criptografados/
│   ├── recuperados/
│   └── evidencias/
├── keylogger-lab/
│   ├── simulador_keylogger.py
│   ├── envio_smtp.py
│   ├── registro_teclas.txt
│   ├── README.md
│   └── evidencias/
├── .gitignore
└── README.md
```

## 7. Conclusão

Os dois laboratórios permitiram estudar, de maneira prática e controlada, características associadas ao funcionamento de ransomware e keyloggers.

A simulação de ransomware demonstrou a transformação e a recuperação de arquivos, enquanto a simulação de keylogger demonstrou o registro de entradas fictícias e sua transmissão por SMTP local.

As atividades contribuíram para a compreensão dos riscos associados a esses tipos de malware e da importância das medidas preventivas de segurança.

Este projeto foi desenvolvido como parte das atividades práticas do curso de Cibersegurança Santander/DIO, com base nos conhecimentos transmitidos pela professora **Isadora Ferrão**, cujas orientações contribuíram para a compreensão dos riscos associados a esses tipos de malware e para a importância da adoção de medidas preventivas.

**Aviso:** este projeto possui finalidade exclusivamente educacional. Os programas foram desenvolvidos para simulações controladas e não devem ser utilizados para coletar informações sem autorização ou comprometer sistemas de terceiros.
