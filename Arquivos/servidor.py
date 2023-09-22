# type: ignore[assignment]
import rpyc # biblioteca para Python RPC
from rpyc.utils.server import ThreadedServer 
import requests as rs # requisições Web
import json # tratamento do JSON

class MyService(rpyc.Service):
    def exposed_echo(self, text):
        print(text)

    def exposed_imc(self, peso, altura):
        calculo = float(peso) / float(altura) *float(altura)
        classificacao = ""

        if(calculo < 18,5):
            classificacao = "Magreza"
        elif(18,5 < calculo < 24,9):
            classificacao = "Normal"
        elif(25 < calculo < 29,9):
            classificacao = "Sobrepeso"
        elif(30  > calculo < 34,9):
            classificacao = "Obesidade grau I"
        elif(35 > calculo < 39,9):
            classificacao = "Obesidade grau II"
        elif(18,5 > calculo < 24,9):
            classificacao = "Normal"
        elif(18,5 > calculo < 24,9):
            classificacao = "Normal"
        elif(calculo > 40):
            classificacao = "Obesidade grau III"
        
        return calculo, classificacao

if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='0.0.0.0', port = 18812)
    print('Servidor online')
    server.start()
