from cryptomarketcap import Crypto

#EXAMPLE

#Portfolio tracker
#Declare cryptoassets in this dictionary along with the number owned

portfolio={"bitcoin": 1, "ethereum": 2, "litecoin": 1, "iota": 20, "ripple": 40, "cardano": 20}
currency = "GBP"

total = 0

#this for-loop iterates through the keys and values in the portfolio dictionary

for coin, holdings in portfolio.items():
    #create each cryptocurrency object from which to gather their attributes
    #this will return the cryptoasset prices in GBP
    coinObj = Crypto(coin, currency)
    v = holdings*coinObj.price
    total += v
    print("%s: %s %s" % (coin.title(), v, currency))

print("Your total holdings: %s in %s" % (total, currency))
