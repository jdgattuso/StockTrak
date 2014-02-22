import easygui as eg
import urllib
import os

while 1:

    enterboxer = eg.enterbox(msg='', title='Enter stock symbol')
    nname = urllib.urlopen('http://finance.yahoo.com/d/quotes.csv?s='+enterboxer+'&f=n')
    bbidaask = urllib.urlopen('http://finance.yahoo.com/d/quotes.csv?s='+enterboxer+'&f=ba')
    cchange = urllib.urlopen('http://finance.yahoo.com/d/quotes.csv?s='+enterboxer+'&f=m5m7')
    name = nname.read() 
    bidask = bbidaask.read()
    change = cchange.read()
    eg.msgbox('Name'+ name + 'bid,ask' + ' '+ bidask + '200, 50 day moving avg % change' + ' ' +change, 'results')
    restart = eg.ynbox('Do you want to restart?', 'Restart', choices=('Yes', 'No'))
    if restart == 1:
        pass
    else:
        exit()
    

    