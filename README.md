# 📝 Gerenciador de Tarefas

Gerenciador de tarefas desenvolvido em Python com SQLite, rodando diretamente no terminal.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) ![Projeto de estudo](https://img.shields.io/badge/Projeto-de%20estudo-blue)

---

## ✨ O que ele faz

- Adiciona novas tarefas
- Lista todas as tarefas cadastradas com seus respectivos IDs
- Remove tarefas pelo número identificador
- Permite definir um título personalizado para a aplicação
- Salva as tarefas e configurações automaticamente no banco de dados

## 🚀 Como rodar

Precisa apenas do Python 3 instalado. Não é necessário instalar bibliotecas externas.

```bash
python main.py
```

O banco de dados (`tarefas.db`) é criado automaticamente na primeira execução.

## 📋 Menu

| **Opção** | **Ação** |
|---|---|
| **1** | Adicionar tarefa |
| **2** | Ver tarefas |
| **3** | Remover tarefa |
| **sair** | Encerrar o programa |

## 🖥️ Exemplo de uso

```text
Digite o título da página: Minhas tarefas

MINHAS TAREFAS

1 Adicionar tarefa
2 Ver tarefas
3 Remover tarefa

Escolha uma das opções: 1
Digite a tarefa: Estudar Python
Tarefa adicionada!

1 Adicionar tarefa
2 Ver tarefas
3 Remover tarefa

Escolha uma das opções: 2
1. Estudar Python
```

## 🧠 Competências praticadas

- Laços de repetição (`while`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Entrada e saída de dados (`input` e `print`)
- Tratamento de erros com `try` e `except`
- Banco de dados SQLite: `CREATE TABLE`, `INSERT`, `SELECT` e `DELETE`
- Consultas parametrizadas (`?`)
- Criação e manipulação de tabelas
- Persistência de dados
- Integração entre Python e SQLite

## 📁 Banco de dados

O projeto utiliza duas tabelas:

- `tarefas`: armazena o ID e a descrição das tarefas.
- `configuracoes`: armazena o título personalizado da aplicação.

As informações permanecem salvas mesmo após o encerramento do programa.

---

Projeto desenvolvido para praticar Python, SQL e manipulação de banco de dados.
