import web_crawler_bs4 as web_crawler
import db_handler
import numpy as np
import time
import datetime
# from finsymbols import symbols
import get_nasdaq_symbols


def create_data(stock_symbol,links,web_page,titles):
    data = list()
    for link, title in zip(links,titles):
        d = [stock_symbol, link, web_page, title]
        data.append(d)

    return data

web_page = ["https://seekingalpha.com/","https://finance.yahoo.com/","http://www.cnbc.com/","https://www.bloomberg.com/"]
symbol_suffix = 'symbol/'
stock_symbols = ["AMAT",'BOFI','BBRY','C']
words = [['Applied Materials','AMAT'],['BofI Holding','BOFI'],['BlackBerry','BBRY'],'Citi']


# stock_symbols, words = get_nasdaq_symbols.get_list()

data = []

for stock, word in zip(stock_symbols,words):
    # stock = stock_sym['symbol']
    #  word = stock_sym['symbol']
    for page in web_page:
        if page is 'https://seekingalpha.com/':
            url = page + symbol_suffix + stock + "?s=" + stock.lower()
            dynamic_page = False
        elif page is 'https://finance.yahoo.com/':
            url = page + 'quote/' + stock + '?p=' + stock
            dynamic_page = True
        elif page is 'http://www.cnbc.com/':
            url = page + 'quotes/?symbol=' + stock + '&tab=news'
            dynamic_page = False
        elif page is 'https://www.bloomberg.com/':
            url = page + 'quote/' + stock + ':US'
            dynamic_page = False

        # get links
        links, titles = web_crawler.spider(page, url, word, dynamic_page)
        print(page + ' - ' + stock + " found " + str(len(links)) + ' links')
        if links:
            print('adding to db')
            data.append(create_data(stock, links, page, titles))
        else:
            print('empty link')



# write links to db
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y%m%d-%H%M%S'))
name = 'stocks' + date + '.db'

name = 'stocks_db.db'
data = np.array(data).T.tolist()

DB = db_handler.DB_Handler()
DB.build_new_db(name,data)

