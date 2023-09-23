# Importando a biblioteca RPyC para Python, que permite comunicação RPC.
import rpyc

# Estabelecendo uma conexão RPC com o servidor usando o endereço IP e a porta.
request = rpyc.connect("20.127.212.32", 18812)

# Solicitando que o usuário escolha uma opção.
options = int(input("1. IMC (Índice de Massa Corporal)\n2. Equações do 2° grau\n3. Verificação de Palíndromo\nOpção: "))

if options == 1:
    # Opção para calcular o IMC (Índice de Massa Corporal).
    weight = float(input("Digite seu peso [Kg]: "))
    height = float(input("Digite sua altura [Metros]: "))
    response = request.root.imc(weight, height)

    print(f"IMC para peso {weight:.2f} Kg e altura {height:.2f} é {response[0]:.2f} kg/m2")
    print(f"Classificação: {response[1]}")

if options == 2:
    # Opção para resolver uma equação quadrática.
    a = int(input("Digite o coeficiente a: "))
    b = int(input("Digite o coeficiente b: "))
    c = int(input("Digite o coeficiente c: "))

    response = request.root.equation(a, b, c)

    print(f"Delta: {response[0]}")
    print(f"Primeira raiz: {response[1]}")
    print(f"Segunda raiz: {response[2]}")
    print("Soluçao: s={%d, %d}" %(response[1], response[2]))

if options == 3:
    # Opção para verificar se uma palavra é um palíndromo.
    word = input("Digite uma palavra para verificar se é um palíndromo: ")

    response = request.root.palindrome(word)

    print(response)
