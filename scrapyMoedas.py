from bs4 import BeautifulSoup
import requests
import re

# Conecta com o site
link = "https://coinmarketcap.com/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")

tbody = site.find("tbody")
linhas = tbody.find_all("tr")
moedas = {}

for linha in linhas:
    try:
        nome = linha.find(class_="iPbTJf").text
        codigo = linha.find(class_="coin-item-symbol").text
        valores = linha.find_all(string=re.compile(r"\$"))
        preco = valores[0]
        percentuais = linha.find_all(string=re.compile("%"))
        
        for i, percentual in enumerate(percentuais):
            if "ivvJzO" in percentual.parent["class"]:
                percentuais[i] = '-' + str(percentual)

        var_1h = percentuais[0]
        var_24h = percentuais[1]
        var_7d = percentuais[2]
        market_cap = valores[2]
        volume = valores[3]
        dic = { "nome": nome, "codigo": codigo, "preco": preco, "var_1h": var_1h, "var_24h": var_24h, "var_7d": var_7d, "market_cap": market_cap, "volume": volume }
        moedas[nome] = dic
    except AttributeError:
        break
