from flask import Flask, render_template
from web3 import Web3
import requests
import json
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Conectar ao provedor de Ethereum usando o endpoint fornecido
infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar se estamos conectados ao provedor
if web3.isConnected():
    print("Conectado ao Ethereum")
else:
    print("Erro ao conectar ao Ethereum")

# Endereço MetaMask
# Exemplo de endereço Ethereum em formato não-checksum
address = '0x4a4a953c0662bfc94d9f03f3c3d3b4af01537cfc'

# Convertendo para checksum address
checksum_address = Web3.toChecksumAddress(address)

# Agora use o checksum_address onde você precisar no seu código Web3.py
balance = web3.eth.get_balance(checksum_address)

# Função para verificar o saldo da carteira
def check_balance(address):
    balance = web3.eth.get_balance(address)
    ether_balance = web3.fromWei(balance, 'ether')
    return ether_balance

# Função para obter o número do bloco atual
def get_block_number():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    response = requests.post(infura_url, headers=headers, data=json.dumps(data))
    block_number = int(response.json()['result'], 16)
    return block_number

@app.route('/')
def index():
    balance = check_balance(checksum_address)
    block_number = get_block_number()
    return render_template('index.html', balance=balance, block_number=block_number)

if __name__ == '__main__':
    app.run(debug=True)
