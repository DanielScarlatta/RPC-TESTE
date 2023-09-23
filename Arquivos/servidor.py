# Importa a biblioteca RPyC para Python, que permite comunicação RPC
import rpyc

# Importa a classe ThreadedServer do módulo server do pacote rpyc.utils.
# Essa classe é usada para criar um servidor RPC que pode lidar com várias solicitações simultaneamente usando threads.
from rpyc.utils.server import ThreadedServer

# Define a classe MyService, que implementa os métodos expostos no servidor RPC.
class MyService(rpyc.Service):

    # Método exposto para calcular o Índice de Massa Corporal (IMC).
    def exposed_imc(self, weight, height):
        calculation = float(weight) / (float(height) * float(height))
        classification = ""  

        # Determina a classificação do IMC com base no valor calculado.
        if calculation < 18.5:
            classification = "Abaixo do peso"
        elif 18.5 <= calculation < 24.9:
            classification = "Peso normal"
        elif 25 <= calculation < 29.9:
            classification = "Sobrepeso"
        elif 30 <= calculation < 34.9:
            classification = "Obesidade Classe I"
        elif 35 <= calculation < 39.9:
            classification = "Obesidade Classe II"
        elif calculation >= 40:
            classification = "Obesidade Classe III"
        
        # Retorna o valor do IMC e sua classificação.
        return calculation, classification
    
    # Método exposto para resolver uma equação quadrática.
    def exposed_equation(self, a, b, c):
        delta = (b * b) - 4 * a * c
        
        # Calcula as raízes da equação quadrática.
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)

        # Retorna o valor do delta e as raízes.
        return delta, x1, x2
    
    # Método exposto para verificar se uma palavra é um palíndromo.
    def exposed_palindrome(self, text):
        # Remove espaços em branco e converte a string para letras minúsculas.
        text = text.replace(" ", "").lower()
        # Inverte a string.
        reversed_text = text[::-1]
        palindrome_result = "" 

        # Verifica se a string é um palíndromo comparando-a com sua versão invertida.
        if reversed_text == text:
            return "Palíndromo: " + reversed_text  # Retorna a string invertida    
        else:
            palindrome_result = "Não é um palíndromo"
            return palindrome_result  # Retorna a mensagem indicando que não é um palíndromo   

# Inicialização do servidor RPC.
if __name__ == "__main__":
    # Cria um servidor RPC que escuta em todas as interfaces ('0.0.0.0') e na porta 18812.
    server = ThreadedServer(MyService, hostname='0.0.0.0', port=18812)
    print('Servidor online')
    # Inicia o servidor.
    server.start()
