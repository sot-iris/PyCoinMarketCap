from cryptomarketcap import Crypto

#EXAMPLE

#Portfolio tracker
#Declare cryptoassets in this dictionary along with the number owned

portfolio={"bitcoin": 100, "ethereum": 2000, "litecoin": 80, "iota": 1900, "ripple": 20000, "cardano": 20000}
currency = "GBP"

total = 0

#this for-loop iterates through the keys and values in the portfolio dictionary

for coin, holdings in portfolio.items():
    #create each cryptocurrency object from which to gather their attributes
    #this will return the cryptoasset prices in GBP
    coin = Crypto(coin, holdings)
    v = value*coin.price
    total += v
    print("%s: %s %s" % (coin.title(), v, currency))

print("Your total holdings: %s in %s" % (total, currency))
