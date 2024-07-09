# My Ethereum App

## Descrição

Este é um projeto de aplicação Ethereum que interage com a blockchain usando a API da Infura e a biblioteca Web3.py. A aplicação inclui funcionalidades básicas de consulta de saldo e transação de tokens.

## Funcionalidades

- Consulta de saldo de uma conta Ethereum.
- Envio de transações Ethereum.
- Interação com contratos inteligentes.

## Tecnologias Utilizadas

- **Python 3.10**: Linguagem de programação principal.
- **Web3.py**: Biblioteca para interação com a blockchain Ethereum.
- **Infura**: API para acesso à blockchain Ethereum.
- **Python-dotenv**: Para gerenciamento de variáveis de ambiente.

## Instalação

### Pré-requisitos

- Python 3.10 ou superior.
- pip (gerenciador de pacotes do Python).

### Passos para instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/AstridNielsen-lab/my_eth_app.github.io.git
    cd my_eth_app
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas Unix
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` com as seguintes variáveis:

    ```env
    infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    ADDRESS = "YOUR_ETHEREUM_ADDRESS"
    ```

## Uso

1. Ative o ambiente virtual, se ainda não estiver ativo:

    ```bash
    source venv/bin/activate  # Para sistemas Unix
    venv\Scripts\activate  # Para Windows
    ```

2. Execute o script principal:

    ```bash
    python main.py
    ```

## Estrutura do Projeto

```plaintext
my_eth_app/
├── venv/                   # Ambiente virtual
├── .env                    # Variáveis de ambiente (não comitar)
├── .gitignore              # Arquivos e pastas a serem ignorados pelo git
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
├── main.py                 # Script principal da aplicação
└── ...                     # Outros scripts e arquivos do projeto

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/fooBar`).
3. Faça commit das suas alterações (`git commit -am 'Add some fooBar'`).
4. Faça push para a branch (`git push origin feature/fooBar`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

### Imagens

![Tela](https://raw.githubusercontent.com/AstridNielsen-lab/my_eth_app.github.io/main/Ethereum%20Wallet%20Info%20code.png)

![Código](https://raw.githubusercontent.com/AstridNielsen-lab/my_eth_app.github.io/main/Ethereum%20Wallet%20Info%20code.png)
