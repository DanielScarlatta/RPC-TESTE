import rpyc
import subprocess

# Comando para instalar o pacote rpyc
command = "pip install rpyc"

try:
    # Executar o comando pip
    subprocess.run(command, shell=True)
    print("O pacote rpyc foi instalado com sucesso.")
except Exception as e:
    print("Ocorreu um erro durante a instalação do pacote rpyc:")
    print(str(e))


# # Instala a biblioteca RPC + Plumbum
# !pip install rpyc

# biblioteca RPC do Python

# Chamada RPC para o Azure
requisicao = rpyc.connect("20.127.212.32", 18812)

# leitura do teclado para as opções
op = int(input("1. Consultar CEP\n2. Somar\n3. Subtrair\nOpção: "))

if op == 1:
    cep = input("Informe o CEP: ")
    # executando a chamada remota RPC
    retorno = requisicao.root.cep(cep)

    # melhorar a saída do CEP
    endereco = retorno['address']
    cidade = retorno['city']
    estado = retorno['state']
    bairro = retorno['district']

    print(endereco)
    print(f'{cidade}/{estado}')
    print(bairro)

elif op == 2:  # elif é igual ao else if
    # soma entre dois valores
    v1 = int(input("Digite o valor 1: "))
    v2 = int(input("Digite o valor 2: "))
    retorno = requisicao.root.soma(v1, v2)
    print(f'A soma entre {v1} e {v2} é: {retorno}')

elif op == 3:  # elif é igual ao else if
    # subtração entre dois valores
    v1 = int(input("Digite o valor 1: "))
    v2 = int(input("Digite o valor 2: "))
    retorno = requisicao.root.subtracao(v1, v2)
    print(f'A subtração entre {v1} e {v2} é: {retorno}')

    # Teste carregando o CEP via uma API dentro do Python
''' import requests as rs
x = rs.get('https://cep.awesomeapi.com.br/json/03590130')
import json
print(json.loads(x.text)['address'])
print(json.loads(x.text)['city'])
print(json.loads(x.text)['state'])
print(json.loads(x.text)['district']) '''

requisicao = rpyc.connect("20.127.212.32", 18812)
x = requisicao.root.echo(['rpcDaniel', 'scar123'])
x