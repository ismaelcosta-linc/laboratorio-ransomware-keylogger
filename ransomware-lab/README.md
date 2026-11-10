# Laboratório de Ransomware Simulado

## 1. Objetivo

Desenvolver um simulador educacional em Python para demonstrar a transformação reversível de arquivos, a recuperação de dados e a importância de medidas preventivas contra ransomware.

O experimento utiliza exclusivamente arquivos fictícios em um ambiente controlado.

## 2. Ambiente e ferramentas

- Sistema operacional: Debian GNU/Linux 13
- Linguagem: Python 3.13.5
- Técnica: XOR com chave fixa, para fins didáticos
- Ferramentas: terminal Linux e SHA-256

## 3. Procedimento

1. Criação de dois documentos fictícios (`documento.txt` e `relatorio.txt`).
2. Desenvolvimento do programa `simulador.py`.
3. Criação de cópias dos documentos originais.
4. Transformação reversível das cópias utilizando XOR.
5. Geração de arquivos com extensão `.simulado`.
6. Criação automática da nota de resgate simulada (`criptografados/LEIA-ME.txt`), a partir de `modelo-nota-resgate.txt`.
7. Recuperação dos documentos utilizando a mesma chave.
8. Comparação dos hashes SHA-256 dos arquivos originais e recuperados.
9. Análise da nota educativa, que menciona a professora Isadora Ferrão e os riscos de pagar resgates.

## 4. Evidências e resultados

O simulador executou corretamente as operações de cópia, transformação e recuperação dos dois documentos.

A comparação dos hashes SHA-256 confirmou que os arquivos recuperados são idênticos aos originais, sem perda de dados.

A nota `LEIA-ME.txt` foi criada automaticamente durante a execução, sem impedir a recuperação dos documentos.

**Evidências registradas:**

- `evidencias/execucao-simulador.txt`: registro da execução.
- `evidencias/hashes-sha256.txt`: hashes dos arquivos originais e recuperados.
- `mensagem-simulada.txt`: mensagem educativa do experimento.
- `modelo-nota-resgate.txt`: modelo utilizado para gerar a nota simulada.
- `criptografados/LEIA-ME.txt`: nota criada automaticamente pelo simulador.

## 5. Medidas preventivas

Entre as principais medidas de proteção contra ransomware estão:

- Manter backups periódicos, preferencialmente com cópias isoladas ou offline.
- Utilizar antivírus e ferramentas de proteção atualizadas.
- Manter o sistema operacional e os aplicativos atualizados.
- Evitar executar arquivos ou abrir anexos de origem desconhecida.
- Utilizar ambientes isolados para analisar programas suspeitos.
- Aplicar o princípio do menor privilégio aos usuários.

## 6. Conclusão

O experimento demonstrou o funcionamento básico de uma transformação reversível de arquivos e sua posterior recuperação.

A verificação por SHA-256 comprovou a integridade dos documentos recuperados.

A técnica XOR com chave fixa foi utilizada exclusivamente para fins didáticos e não representa a criptografia robusta normalmente empregada por ransomware real.

Nenhum arquivo pessoal foi afetado, e o programa não realiza propagação, cobrança ou comunicação externa.

**Projeto educacional desenvolvido no contexto do curso de Cibersegurança Santander/DIO, com auxílio do chatbot do ChatGPT.**
