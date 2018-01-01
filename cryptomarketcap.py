import requests

class Crypto:
    def __init__(self, id, price_in):
        getinfo = requests.get("https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s" % (id, price_in))
        firstindex = getinfo.json()
        self.id = id.title()
        self.info = firstindex[0]
        self.price_usd = float(self.info["price_usd"])
        self.price = float(self.info["price_%s" % (price_in.lower())])
        self.market_cap_usd = float(self.info["market_cap_usd"])

