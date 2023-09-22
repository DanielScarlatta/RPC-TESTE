# biblioteca RPC do Python
import rpyc

# Chamada RPC para o Azure
request = rpyc.connect("20.127.212.32", 18812)

# leitura do teclado para as opções
# options = int(input("1. Consultar CEP\n2. Somar\n3. Subtrair\nOpção: "))
options = int(input("1. imc\nOpção: "))

# if options == 1:
#     cep = input("Informe o CEP: ")
#     # executando a chamada remota RPC
#     returnCall = request.root.cep(cep)

#     # melhorar a saída do CEP
#     endereco = returnCall['address']
#     cidade = returnCall['city']
#     estado = returnCall['state']
#     bairro = returnCall['district']

#     print(endereco)
#     print(f'{cidade}/{estado}')
#     print(bairro)

# elif options == 2:  # elif é igual ao else if
#     # soma entre dois valores
#     v1 = int(input("Digite o valor 1: "))
#     v2 = int(input("Digite o valor 2: "))
#     returnCall = request.root.soma(v1, v2)
#     print(f'A soma entre {v1} e {v2} é: {returnCall}')

# elif options == 3:  # elif é igual ao else if
#     # subtração entre dois valores
#     v1 = int(input("Digite o valor 1: "))
#     v2 = int(input("Digite o valor 2: "))
#     returnCall = request.root.subtracao(v1, v2)
#     print(f'A subtração entre {v1} e {v2} é: {returnCall}')

if options == 1:
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))

  resposta = request.root.imc(peso, altura)

  print("o imc do peso %.2f e altura %.2f é %.2f  \n Classificação: %s" %(peso, altura, resposta[0], resposta[1]))

# chama a função de imprimir no servidor informa quem acessou

x = request.root.echo(['Daniel', 'aluno'])
x