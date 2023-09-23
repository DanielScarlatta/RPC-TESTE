# type: ignore[assignment]
import rpyc # biblioteca para Python RPC
from rpyc.utils.server import ThreadedServer 
import requests as rs # requisições Web
import json # tratamento do JSON

class MyService(rpyc.Service):

    def exposed_imc(self, peso, altura):
        calculo = float(peso) / (float(altura) * float(altura))
        classificacao = ""

        if(calculo < 18.5):
            classificacao = "Magreza"
        elif(calculo < 24.9 and calculo > 18.5):
            classificacao = "Normal"
        elif(calculo < 29.9 and calculo > 24.9):
            classificacao = "Sobrepeso"
        elif(calculo < 34.9 and calculo >  29.9):
            classificacao = "Obesidade grau I"
        elif(calculo < 39.9 and calculo > 34.9):
            classificacao = "Obesidade grau II"
        elif(calculo > 40):
            classificacao = "Obesidade grau III"
        
        return calculo, classificacao
    
    def exposed_palindromo(self, text):
        text = text.replace(" ", "").lower()
        inverso = text[::-1]
        palindromo = ""


        if (inverso == text):
            return inverso
            
        else:
            palindromo = "Nao é um palíndromo"
            return palindromo
        

if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='0.0.0.0', port = 18812)
    print('Servidor online')
    server.start()

