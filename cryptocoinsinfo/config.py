import os

# the token of the @Degen_Light_Bot
TOKEN_BOT = '6249108534:AAFV-jPIRbqN6KsmsGdkp0hx2fYxJaNy-Hk'

YOUR_TELEGRAM_ALIAS = 'Degen_Light_Bot'

# do APIs requests with pause
TIME_INTERVAL = 3600

# old CoinMarketCap public API
# COINMARKET_API_URL_COINLIST = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'

# new pro API
CMC_API_KEY = "3f2e222b-a945-4835-a0b8-3da41e3eb5a6"
COINMARKET_API_URL_COINLIST = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000' \
                              '&CMC_PRO_API_KEY={}'

# CryptoCompare API
# is used to search up if requested coin is on the CC coinlist
CRYPTOCOMPARE_API_URL_COINLIST = 'https://min-api.cryptocompare.com/data/all/coinlist'
# is used to parse prices of the requested coin
CRYPTOCOMPARE_API_URL_PRICEMULTIFULL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=BTC,USD'

FILE_JSON_COINMARKET = os.path.dirname(os.path.realpath(__file__)) + '/coinmarketcoins.json'
FILE_JSON_CRYPTOCOMPARE = os.path.dirname(os.path.realpath(__file__)) + '/cryptocomparecoins.json'


class JSONFiles:
    def __init__(self):
        self.coinmarketcapjson = {}
        self.cryptocomparejson = {}

    def update_cmc_json(self, json1):
        assert isinstance(json1, dict)
        self.coinmarketcapjson = json1
        return json1

    def update_cc_json(self, json2):
        assert isinstance(json2, dict)
        self.cryptocomparejson = json2
        return json2


# the object of class JSONFiles for save json API coins lists
jsonfiles = JSONFiles()
