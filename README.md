# LAD.Py — Sistema de Votação Digital
Projeto Integrador I — Engenharia de Software | PUC Campinas  
Prof. Dr. Luã Marcelo Muriana | 2026

---

## Descrição

O **LAD.Py** é um sistema de votação digital com finalidade exclusivamente didática, executado via terminal. O projeto integra Python, MySQL e criptografia por **Cifra de Hill** para proteger dados sensíveis, simulando um ecossistema eleitoral completo com três módulos principais:

- **Gerenciamento** — cadastro, edição, remoção, busca e listagem de eleitores e candidatos, com validação matemática de CPF e Título de Eleitor e geração automática de chave de acesso criptografada.
- **Votação** — abertura da urna com autenticação do mesário, Zerézima, coleta de votos com emissão de protocolo criptografado e encerramento com dupla confirmação.
- **Auditoria e Resultados** — logs de ocorrências, boletim de urna, estatísticas de comparecimento, votos por partido e validação de integridade.

---

## Integrantes

- Arthur Peripolli
- Beatriz Valadares
- Letícia Leme
- Luisa Moraes
- Sabrina Prates

---

## Tecnologias Utilizadas

- Python 3.10+
- MySQL Server 8.0+
- Bibliotecas: `mysql-connector-python`, `datetime`, `random`, `os`
- Ferramentas: VS Code, MySQL Workbench, GitHub

---

## Como Executar

**1. Instale a dependência:**
```bash
pip install mysql-connector-python
```

**2. Configure o banco de dados:**  
Execute o arquivo `Database/banco_dados.sql` no MySQL Workbench para criar o banco `tabela_bd`.

**3. Configure a conexão:**  
Abra `conexao.py` e ajuste `host`, `user`, `password` e `database` com suas credenciais.

**4. Execute o sistema:**
```bash
python main.py
```

---

> Este projeto é uma simulação acadêmica e não possui relação com sistemas de votação utilizados em processos eleitorais reais.