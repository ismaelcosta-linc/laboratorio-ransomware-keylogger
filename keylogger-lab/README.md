# Laboratório de Keylogger Simulado

## 1. Objetivo

Este laboratório foi desenvolvido como parte do curso de Cibersegurança Santander/DIO, com o objetivo de demonstrar de maneira controlada e simulada um funcionamento básico do registro de entradas de texto e da transmissão desses registros através de e-mails.

Foi desenvolvido um simulador em Python, utilizando entradas de texto pelo usuário com dados fictícios, sem realizar captura oculta de teclas ou monitoramento de outras aplicações.

## 2. Ambiente utilizado

- Sistema operacional: Debian GNU/Linux 13
- Linguagem: Python 3
- Servidor SMTP local: aiosmtpd 1.4.6
- Endereço: 127.0.0.1
- Porta: 8025

O experimento foi executado localmente, sem utilizar contas de e-mail reais ou serviços externos.

## 3. Desenvolvimento

O laboratório foi dividido em duas partes.

**Registro de entradas**

O programa `simulador_keylogger.py` solicita voluntariamente textos fictícios pelo terminal e registra cada entrada no arquivo `registro_teclas.txt`, acompanhada de data e horário.

O comando `SAIR` encerra a execução.

**Simulação de envio por e-mail**

O programa `envio_smtp.py` lê o arquivo de registros e transmite seu conteúdo para um servidor SMTP local.

Foi utilizado o endereço fictício `destinatario@laboratorio.test`, sem autenticação em serviços externos.

O servidor foi iniciado com o comando:

```bash
python3 -m aiosmtpd -n -l 127.0.0.1:8025
```

O envio foi realizado manualmente por meio de:

```bash
python3 envio_smtp.py
```

## 4. Testes e resultados

**Teste 1 — Registro de entradas**

Foram inseridas três entradas fictícias pelo terminal.

Resultado: os dados foram armazenados corretamente no arquivo `.txt`, acompanhados de data e horário.

**Teste 2 — Comunicação SMTP**

Com o servidor SMTP local ativo, o programa realizou o envio dos registros.

Resultado: a mensagem foi recebida corretamente pelo servidor, contendo os três registros fictícios.

**Teste 3 — Falha de comunicação**

O servidor SMTP foi encerrado e o programa de envio executado novamente.

Resultado:

```text
Falha no envio: [Errno 111] Connection refused
```

A falha era esperada, pois não havia um servidor disponível para receber a conexão.

## 5. Evidências

Os arquivos do laboratório estão organizados da seguinte forma:

```text
keylogger-lab/
├── simulador_keylogger.py
├── envio_smtp.py
├── registro_teclas.txt
├── evidencias/
│   ├── registro_teste.txt
│   └── teste_smtp.txt
└── README.md
```

- `registro_teste.txt`: cópia dos registros fictícios utilizados no experimento.
- `teste_smtp.txt`: documentação dos resultados de comunicação SMTP.

## 6. Funcionamento de um keylogger real

Diferentemente do simulador desenvolvido, um keylogger malicioso pode registrar entradas do teclado sem o conhecimento ou consentimento do usuário.

Dependendo de sua implementação, esse tipo de programa pode operar em segundo plano, monitorar diferentes aplicações e transmitir informações coletadas para sistemas externos.

Essas características foram abordadas apenas teoricamente, não sendo implementadas no laboratório.

## 7. Medidas preventivas

Entre as principais medidas de proteção contra keyloggers estão:

- Manter o sistema operacional e os aplicativos atualizados.
- Evitar executar programas de origem desconhecida.
- Utilizar ferramentas de proteção e monitoramento.
- Aplicar o princípio do menor privilégio.
- Monitorar processos e conexões de rede suspeitas.
- Utilizar firewall para restringir comunicações não autorizadas.
- Utilizar autenticação multifator, preferencialmente resistente a phishing.

O firewall pode auxiliar na prevenção da transmissão de dados para destinos não autorizados. Entretanto, seu uso isolado não garante proteção contra keyloggers.

O teste de conexão recusada realizado neste laboratório não representa um bloqueio por firewall, mas demonstra a dependência da comunicação em relação à disponibilidade do servidor de destino.

## 8. Conclusão

O experimento demonstrou o registro voluntário de informações fictícias e sua posterior transmissão por meio de um servidor SMTP local.

Os testes confirmaram o armazenamento dos registros, o recebimento da mensagem e o comportamento do programa diante da indisponibilidade do servidor.

O laboratório permitiu compreender conceitos associados ao funcionamento de keyloggers e à transmissão de dados, sem implementar mecanismos de captura oculta ou comunicação externa.

Este projeto foi desenvolvido exclusivamente para fins de testes e simulações para atividade do curso, com auxílio do chatbot do ChatGPT, como parte das atividades práticas do curso Santander/DIO.
