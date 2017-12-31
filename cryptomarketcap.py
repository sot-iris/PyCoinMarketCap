import requests

class Crypto:
    def __init__(self, id, price_in):
        self.id = id.title()
        self.price_in = price_in
        self.getinfo = requests.get("https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s" % (self.id, self.price_in))
        firstindex = self.getinfo.json()
        self.info = firstindex[0]
        self.price_usd = float(self.info["price_usd"])
        self.price_gbp = float(self.info["price_gbp"])
        self.market_cap_usd = float(self.info["market_cap_usd"])

