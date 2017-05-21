import web_crawler_bs4 as web_crawler
import db_handler
import numpy as np


def create_data(stock_symbol,links,web_page):
    data = list()
    for link in links:
        d = [stock_symbol, link, web_page]
        data.append(d)

    return data


web_page = "https://seekingalpha.com/"
web_page = ["https://seekingalpha.com/","https://finance.yahoo.com/","http://www.cnbc.com/finance/","https://www.bloomberg.com/"]
symbol_suffix = 'symbol/'
stock_symbol = ["AMAT",'BOFI','BBRY','C']
words = ['Applied Materials','BofI Holding','BlackBerry','Citigroup']

data = []

for stock, word  in zip(stock_symbol, words):
    url = web_page + symbol_suffix + stock + "?s=" + stock.lower()
    # get links
    links = web_crawler.spider(web_page, url, word)
    data.append(create_data(stock,links,web_page))

# write links to db
name = 'stocks.db'
DB = db_handler.DB_Handler()
DB.create_db(name)

data = np.array(data).T.tolist()
DB.add_data(data)
