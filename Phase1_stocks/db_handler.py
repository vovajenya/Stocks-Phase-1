import sqlite3

class DB_Handler():
    def create_db(self, name):
        # create a connection. if file doesn't exist, sqlite will create it
        conn = sqlite3.connect(name)

        # cursor
        c = conn.cursor()
        self.conn = conn
        self.c = c

        self.create_table()


    def add_data(self, data):

        for d in data:
            for row in d:
                self.c.execute("INSERT INTO stuffToPlot (stock, link, origin) VALUES (?, ?, ?)",
                               (row[0],row[1],row[2]))
            self.conn.commit()

    def create_table(self):
        # using caps for pure SQL language
        self.c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(stock TEXT, link TEXT, origin TEXT)')



