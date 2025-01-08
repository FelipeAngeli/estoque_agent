# Estoque Agent

O **Estoque Agent** é um sistema de controle de estoque desenvolvido em Python, utilizando frameworks e bibliotecas como Flask, SQLAlchemy e Bootstrap. Este projeto tem como objetivo facilitar o gerenciamento de produtos, fornecedores e movimentações de entrada e saída de itens em um ambiente de estoque.

## Funcionalidades

- **Cadastro de Produtos**: Permite o registro de novos produtos com informações detalhadas, como nome, descrição, preço e quantidade em estoque.
- **Gerenciamento de Fornecedores**: Possibilita a adição e manutenção de dados de fornecedores associados aos produtos.
- **Movimentação de Estoque**: Registra entradas e saídas de produtos, atualizando automaticamente as quantidades disponíveis.
- **Relatórios**: Gera relatórios sobre o status do estoque, incluindo produtos com baixo estoque e histórico de movimentações.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web utilizado para o desenvolvimento do backend.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para gerenciamento do banco de dados.
- **Bootstrap**: Framework CSS para estilização e design responsivo.

## Requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

- Python 3.7 ou superior
- Virtualenv

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/FelipeAngeli/estoque_agent.git
   cd estoque_agent
   ```

2. **Crie um ambiente virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:

   Certifique-se de que o banco de dados esteja configurado corretamente no arquivo de configuração. Execute as migrações para criar as tabelas necessárias:

   ```bash
   flask db upgrade
   ```

5. **Execute a aplicação**:

   ```bash
   flask run
   ```

   A aplicação estará disponível em `http://localhost:5000`.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
estoque_agent/
├── config/           # Arquivos de configuração
├── core/             # Lógica central da aplicação
├── ui/               # Arquivos relacionados à interface do usuário
├── venv/             # Ambiente virtual
├── app.py            # Arquivo principal da aplicação
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests. Para mudanças significativas, por favor, abra primeiro uma issue para discutir o que você gostaria de alterar.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.