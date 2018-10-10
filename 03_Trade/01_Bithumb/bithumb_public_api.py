import requests

curreny = 'ETH'
url = 'https://api.bithumb.com/public/ticker' + curreny

r = requests.get(url)
print (r.json())

