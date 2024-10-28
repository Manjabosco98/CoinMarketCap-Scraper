CoinMarketCap Scraper
Um script em Python que coleta e organiza dados de criptomoedas do site CoinMarketCap, como nome, código, preço, variação percentual e volume de mercado.

Descrição
Este projeto faz web scraping na página principal de listagem de criptomoedas do CoinMarketCap, extraindo informações como:

Nome da moeda e código
Preço atual
Variação percentual em 1h, 24h e 7 dias
Market Cap
Volume de negociação
As informações são organizadas em um dicionário Python, onde cada moeda é uma chave e os detalhes estão disponíveis em um sub-dicionário.

Pré-requisitos
Python 3.x
Bibliotecas: Certifique-se de instalar as seguintes dependências:

pip install requests beautifulsoup4

Como Usar
Clone o repositório e navegue até a pasta do projeto.
Execute o script coin_scraper.py para coletar e exibir os dados das criptomoedas listadas no CoinMarketCap.

python coin_scraper.py

Exemplo de Saída:

{
  "Bitcoin": {
    "nome": "Bitcoin",
    "codigo": "BTC",
    "preco": "$30,000",
    "var_1h": "-0.5%",
    "var_24h": "2.3%",
    "var_7d": "-3.2%",
    "market_cap": "$600B",
    "volume": "$25B"
  },
  ...
}

Funcionalidades
Extração automatizada de dados de moedas em destaque no CoinMarketCap.
Manipulação de strings para obter variações percentuais e preço.
Tratamento de exceções para evitar erros de scraping.
Observações
Este código está sujeito a modificações frequentes no layout do CoinMarketCap, o que pode exigir ajustes futuros no script.
