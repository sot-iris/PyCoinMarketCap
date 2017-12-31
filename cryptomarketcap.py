import requests

class Crypto:
    def __init__(self, id, price_in, sigfig=2):
        self.id = id.title()
        self.price_in = price_in
        self.getinfo = requests.get("https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s" % (self.id, self.price_in))
        firstindex = self.getinfo.json()
        self.info = firstindex[0]
        self.price_usd = round(float(self.info["price_usd"]), sigfig)
        self.price_gbp = round(float(self.info["price_gbp"]), sigfig)
        self.market_cap_usd = round(float(self.info["market_cap_usd"]), sigfig)

