from tkinter import font
import tkinter
import get_nasdaq_symbols
import db_handler
import webbrowser


CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'


# classes
class Listbox(tkinter.Listbox):
    def autowidth(self,maxwidth):
        f = font.Font(font=self.cget("font"))
        pixels = 0
        for item in self.get(0, "end"):
            pixels = max(pixels, f.measure(item))
        # bump listbox size until all entries fit
        pixels = pixels + 10
        width = int(self.cget("width"))
        for w in range(0, maxwidth+1, 5):
            if self.winfo_reqwidth() >= pixels:
                break
            self.config(width=width+w)


# callbacks
def helloCallBack():
    print('hello')

def listCallBack(e):
    # get current selection
    url = Lb1.get(Lb1.curselection())
    # browse to the current selection
    # url = 'http://google.co.kr'
    webbrowser.open(url, new=0)

def selectedItem(e):
    # get the stock symbol
    selected_stock = e

    # open DB
    db_name = 'stocks_db.db'
    DB = db_handler.DB_Handler()
    DB.create_db(db_name)

    # read all related links
    links = DB.get_links(selected_stock)

    # clear the listbox
    Lb1.delete(0, tkinter.END)

    # present the links in the list box
    cnt = 0
    for link in links:
        Lb1.insert(cnt, link[1])
        cnt += 1
    # Lb1.autowidth(250)
# get stocks symbols from db
stock_symbols, words = get_nasdaq_symbols.get_list()


top = tkinter.Tk()

# button
# B = tkinter.Button(top, text ="Hello", command = helloCallBack)

# scrollbar
scrollbar = tkinter.Scrollbar(top)

# list
Lb1 = Listbox(top, yscrollcommand=scrollbar.set)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")


# dropdown menu
variable = tkinter.StringVar(top)
variable.set(stock_symbols[0]) # default value
w = tkinter.OptionMenu(top, variable, *stock_symbols, command=selectedItem)

w.pack()
# B.pack()

Lb1.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
Lb1.bind('<<ListboxSelect>>', listCallBack)
Lb1.config(width=160, height=500)

scrollbar.pack(side=tkinter.LEFT, fill=tkinter.Y)
scrollbar.config(command=Lb1.yview)

top.geometry('{}x{}'.format(1000, 500))
top.resizable(width=False, height=False)
top.mainloop()