# importar o app, importar o Builder (GUI)
# criar o nosso aplicativo
# criar a função build

'Inicialização do Codigo'

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self): #Função padrao para kivy
        return GUI

    def on_start(self): #Quando carregar o app atualiza os valores
        self.root.ids["moeda1"].text = f"Dolar R$ {self.pegar_cotacao('USD')}" #Função do meu app, root o arquivo que é carregar para o Builder, ids é todos os id:
        self.root.ids["moeda2"].text = f"Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R$ {self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link) #cria a requisição
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

MeuAplicativo().run() #looping para o app ficar sempre aberto