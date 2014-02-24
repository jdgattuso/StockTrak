from BeautifulSoup import BeautifulSoup
import urllib

data = []

url = 'http://finance.yahoo.com/etf/'
opener = urllib.urlopen(url)
bs = opener.read()
soup = BeautifulSoup(bs)

for printer in soup.findAll('td', {'class':['tkr', 'mkt3m  align ticker_down', 'mkt3m  align ticker_up']}):    
    data.append(printer.getText())
  
# BeautifulSoup returns unicode: to encode in ascii

print [x.encode('ascii') for x in data]
