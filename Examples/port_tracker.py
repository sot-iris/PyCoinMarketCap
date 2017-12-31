from cryptomarketcap import Crypto

#EXAMPLE

#Portfolio tracker
#Declare cryptoassets in this dictionary along with the number owned
portfolio={"bitcoin": 100, "ethereum": 2000, "litecoin": 80, "iota": 1900, "ripple": 20000, "cardano": 20000}

currency = "GBP"
total = 0

#this for-loop iterates through the keys and values in the portfolio dictionary

for key, value in portfolio.items():
    #create each cryptocurrency object from which to gather their attributes
    #Crypto class: def __init__(self, id, price_in, sigfig=2)
    # id of coin, fiat currency and (optional, default 2 if left empty) number of significant figures for returned price values.
    coin = Crypto(key, currency)
    v = value*coin.price_gbp
    total += v
    print("%s: %s GBP" % (key.title(), v))

print("Your total holdings: %s in %s" % (total, currency))


