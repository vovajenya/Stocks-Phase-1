# sqlite database
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

# create a connection. if file doesn't exist, sqlite will create it
conn = sqlite3.connect('test.db')

# cursor
c = conn.cursor()

# creating a table
def create_table():
    # using caps for pure SQL language
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

# writing data dynamically
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix,date,keyword,value))
    conn.commit()


# reading from db
def read_from_db():
    # selecting all
    #c.execute('SELECT * FROM stuffToPlot')

    # selecting filtered
    #c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='python'")
    #c.execute("SELECT * FROM stuffToPlot WHERE unix>100")
    c.execute("SELECT keyword, unix FROM stuffToPlot WHERE unix>100")

    # printing
    for row in c.fetchall():
        # print specific column
        #print(row[0])
        print(row)


def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


# delete and update db
def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    # [print(row) for row in c.fetchall()]

    # update
    # c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
    # conn.commit()
    #
    # delete
    # c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    # conn.commit()

    c.execute('SELECT * FROM stuffToPlot WHERE value = 6')
    # c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    c.execute('DELETE FROM stuffToPlot WHERE value = 6')
    print(50*'#')
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]






# create_table()
#
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
# read_from_db()
# graph_data()
del_and_update()

c.close()
conn.close()
