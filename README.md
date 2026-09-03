# 💰 Finance-tracker - Controle Financeiro Pessoal

Sistema de controle financeiro pessoal desenvolvido em Flask e SQLite, com registro, categorização e visualização de receitas e despesas.

## 📋 Sobre o projeto

Este projeto foi desenvolvido como parte do meu portfólio, com o objetivo de consolidar conceitos de backend com Flask, modelagem e manipulação de banco de dados relacional (SQLite), e introdução ao uso de JavaScript no frontend.

O sistema permite registrar receitas e despesas, categorizá-las, visualizar um dashboard com saldo e totais, filtrar por mês e acompanhar os gastos por categoria através de um gráfico interativo.

## ✨ Funcionalidades

- ✅ Adicionar receitas e despesas
- ✅ Categorizar despesas (alimentação, transporte, lazer, estudos, outros)
- ✅ Editar e excluir transações
- ✅ Filtrar transações por mês
- ✅ Dashboard com saldo, total de receitas e despesas
- ✅ Visualização de gastos por categoria
- ✅ Gráfico de pizza interativo (Chart.js) mostrando a distribuição de despesas

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal do backend
- **Flask** — framework web
- **SQLite** — banco de dados relacional
- **Jinja2** — engine de templates (integrado ao Flask)
- **HTML5 / CSS3** — estrutura e estilização das páginas
- **JavaScript** — consumo de API e renderização do gráfico
- **Chart.js** — biblioteca de visualização de dados

## 📸 Screenshots

<img width="1900" height="945" alt="image" src="https://github.com/user-attachments/assets/ad5cf8f9-c275-407a-8a0b-499116e9f451" />
<img width="1919" height="944" alt="image" src="https://github.com/user-attachments/assets/d54c4caf-f6fa-4177-900f-8ec915b89ec8" />
<img width="1901" height="943" alt="image" src="https://github.com/user-attachments/assets/74767555-7b92-4062-bbdb-281109a10431" />

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/gustamoraiss/finance-tracker.git
cd finance-tracker
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie o banco de dados:
```bash
python database.py
```

5. Rode a aplicação:
```bash
python app.py
```

6. Acesse no navegador:

http://127.0.0.1:5000


## 🗂️ Estrutura do projeto

```
finance-tracker/
├── app.py # Rotas e lógica principal do Flask
├── database.py # Script de criação do banco de dados
├── requirements.txt # Dependências do projeto
├── static/
│ ├── css/
│ │ └── style.css # Estilização do sistema
│ └── js/
│ └── dashboard.js # Lógica do gráfico (fetch + Chart.js)
├── templates/
│ ├── listar.html # Dashboard e listagem de transações
│ ├── adicionar.html # Formulário de nova transação
│ └── editar.html # Formulário de edição
└── README.md
```


## 📚 O que aprendi com este projeto

- Modelagem de dados relacionais e boas práticas de banco de dados (queries parametrizadas, prevenção de SQL Injection)
- CRUD completo com Flask e SQLite
- Uso de funções de agregação SQL (`SUM`, `GROUP BY`, `COALESCE`) para regras de negócio
- Criação de uma API própria (endpoint JSON) e consumo assíncrono com `fetch`/`async`/`await`
- Integração de uma biblioteca JavaScript externa (Chart.js) para visualização de dados

## 👤 Autor

Desenvolvido por Gustavo Morais — www.linkedin.com/in/gustamoraiss
