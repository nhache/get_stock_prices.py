import urllib.request
import re
import json

stocks = ['AAPL','GOOG']
stock_data = {}
base_url = 'http://finance.yahoo.com/q?s='

def get_stock_data(symbols):
	for symbol in symbols:
		url_add = symbol.lower()
		url = base_url + url_add
		try:
			htmltext = str(urllib.request.urlopen(url).read())
			regex = '<span id="yfs_l84_' + url_add + '">(.+?)</span>'
			pattern = re.compile(regex)
			price = re.findall(pattern, htmltext)
			stock_data[symbol] = price[0]
		except:
			continue
	return json.dumps(stock_data, sort_keys = True)

get_stock_data(stocks)
