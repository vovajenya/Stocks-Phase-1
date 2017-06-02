import web_crawler_bs4 as web_crawler
import db_handler
import numpy as np
import time
import datetime
# from finsymbols import symbols
import get_nasdaq_symbols


def create_data(stock_symbol,links,web_page):
    data = list()
    for link in links:
        d = [stock_symbol, link, web_page]
        data.append(d)

    return data

# s = symbols.get_nasdaq_symbols()
# web_page = "https://seekingalpha.com/"
#web_page = "http://www.cnbc.com/finance/"
# web_page = ["https://seekingalpha.com/","https://www.bloomberg.com/"]
web_page = ["https://seekingalpha.com/","https://finance.yahoo.com/","http://www.cnbc.com/finance/","https://www.bloomberg.com/"]
symbol_suffix = 'symbol/'
stock_symbols = ["AMAT",'BOFI','BBRY','C']
words = [['Applied Materials','AMAT'],['BofI Holding','BOFI'],['BlackBerry','BBRY'],'Citigroup']


stock_symbols, words = get_nasdaq_symbols.get_list()

data = []

# for stock, word  in zip(stock_symbol, words):
try:
    for stock, word in zip(stock_symbols,words):
        # stock = stock_sym['symbol']
        # word = stock_sym['symbol']
        for page in web_page:
            # switch case
            if page is 'https://seekingalpha.com/':
                url = page + symbol_suffix + stock + "?s=" + stock.lower()
            elif page is 'https://finance.yahoo.com/':
                url = page + 'quote/' + stock + '?p=' + stock
            elif page is 'http://www.cnbc.com/finance/':
                url = page + 'quotes/?symbol=' + stock
            elif page is 'https://www.bloomberg.com/':
                url = page + 'quote/' + stock + ':US'

            # get links
            links = web_crawler.spider(page, url, word)
            print(page + ' - ' + stock + " found " + str(len(links)) + ' links')
            if links:
                print('adding to db')
                data.append(create_data(stock,links,page))
            else:
                print('empty link')

except:
    print('operation stopped. saving db...')


# write links to db
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y%m%d-%H%M%S'))
name = 'stocks' + date + '.db'
name = 'stocks_db.db'
DB = db_handler.DB_Handler()
DB.create_db(name)

data = np.array(data).T.tolist()
DB.add_data(data)
