#  Crypto Data Pipeline - Meu Primeiro ETL 

Este é um projeto prático de estudo focado nos fundamentos da Engenharia de Dados. O objetivo principal foi construir uma pipeline **ETL (Extract, Transform, Load)** ponta a ponta, saindo do zero e cravando os dados de forma segura em um banco de dados relacional.

## O que o projeto faz?
O script atua como um "operário" automatizado que:
1. **[E] Extract:** Consome a API pública da CoinGecko para buscar os preços em tempo real do Bitcoin e Ethereum.
2. **[T] Transform:** Trata o JSON recebido, adicionando o *timestamp* (data e hora exata da extração) e estruturando as informações.
3. **[L] Load:** Abre uma conexão segura com um banco PostgreSQL local e salva esses dados na tabela `precos_cripto`.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python 3** (Lógica principal)
* **PostgreSQL** (Banco de dados relacional local)
* **DBeaver** (Gerenciamento e visualização do banco)
* **requests** (Para chamadas de API)
* **psycopg2** (Para a ponte entre Python e PostgreSQL)
* **python-dotenv** (Para gerenciamento seguro de credenciais)
* **uv** (Gerenciador de pacotes e ambientes virtuais ultrarrápido)

## 🛡️ Destaques de Arquitetura e Segurança
Durante o desenvolvimento, não foquei apenas em fazer funcionar, mas em usar boas práticas de mercado:
* **Zero Senhas no Código:** Uso de variáveis de ambiente (`.env`) lidas através da biblioteca `os`, garantindo que credenciais não subam para o GitHub (protegidas pelo `.gitignore`).
* **Proteção contra SQL Injection:** O comando de inserção no banco utiliza *placeholders* (`%s`) via `psycopg2` no lugar de f-strings ou concatenação direta, blindando o banco de dados.
* **Gerenciamento de Conexão:** Abertura e fechamento explícito do `cursor` e da `connection` para evitar vazamento de memória e sobrecarga no servidor do banco.

##  Como rodar na sua máquina

**1. Clone o repositório e instale as dependências:**
Certifique-se de ter o `uv` instalado e rode:
```bash
uv sync

**2. Configure o Banco de Dados e as Credenciais:**

CREATE TABLE IF NOT EXISTS precos_cripto (
    moeda VARCHAR(50),
    valor NUMERIC(15, 6),
    data_extracao TIMESTAMPTZ
);

Em seguida, crie um arquivo chamado .env na raiz do projeto (o mesmo local onde está o seu script) e insira a senha do seu banco de dados sem espaços extras:

DB_PASSWORD=sua_senha_do_postgres_aqui

**3. Execute a Pipeline:**
Com o ambiente pronto, o banco criado e a senha configurada no .env, basta rodar o script principal pelo terminal:

uv run extract.py