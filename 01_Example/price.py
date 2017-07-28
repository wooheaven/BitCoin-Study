import json
import urllib.request
from urllib.request import Request, urlopen

class bithumb:
	urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')
	readTicker = urlTicker.read()
	jsonTicker = json.loads(readTicker)
	FindBTC = jsonTicker['data']['BTC']['closing_price']
	BTC = int(FindBTC)
	FindETH = jsonTicker['data']['ETH']['closing_price']
	ETH = int(FindETH)
	FindDASH = jsonTicker['data']['DASH']['closing_price']
	DASH = int(FindDASH)
	FindLTC = jsonTicker['data']['LTC']['closing_price']
	LTC = int(FindLTC)
	FindETC = jsonTicker['data']['ETC']['closing_price']
	ETC = int(FindETC)
	FindXRP = jsonTicker['data']['XRP']['closing_price']
	XRP = int(FindXRP)
