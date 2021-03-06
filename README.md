# PyCoinMarketCap
A lightweight object-oriented style python wrapper to access http://coinmarketcap.com API

For an alternative, see: https://pypi.python.org/pypi/coinmarketcap/

# Usage

Import the Crypto class
```python
from cryptomarketcap import Crypto
```
The Crypto class takes 2 arguments: the first, *id*, accepts a string of the name of a coin, and the second, *price_in*, the fiat currency from which to convert coin prices to.

For example, the following code will instantiate a crypto class object for bitcoin, whose price will be given in GBP:
We can then access its attributes.
```python
bitcoin = Crypto("bitcoin", "GBP")

#bitcoin.info returns the full json dictionary returned when the API request is made
bitcoin.info

#To print this info in a readable and nice way, simply declare:
bitcoin.information()

#The below returns the price of bitcoin either in the user-specified fiat currency or usd, respectively.
bitcoin.price
bitcoin.price_usd

#Finally, this attribute returns the current market capitalisation of the given cryptocurrency, in this case, bitcoin.
bitcoin.market_cap_usd

```

I will be updating the examples folder with use cases of this Python API wrapper alongside the portolio tracker (annotation for which are hashed within the code).

I hope you find this helpful. 
BTC tips accepted happily: 1NXj1ZZMyNj2DFxVwX4j5sqawjrdSWZ6wg
