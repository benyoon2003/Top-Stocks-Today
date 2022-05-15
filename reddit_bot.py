import string
import praw
from heapq import nlargest
import tkinter as tk
from tkinter import *


class back_end:
    def __init__(self):
        self.stocklst = []
        self.first = None
        self.second = None
        self.third = None

    def get_first_stock(self):
        return self.first

    def get_second_stock(self):
        return self.second

    def get_third_stock(self):
        return self.third

    def create_stock_list(self):
        with open('nasdaq') as f:
            for line in f:
                x = line.split('|')
                self.stocklst.append(x[0])


    def scrape_and_rank(self, pick):
        reddit_read_only = praw.Reddit(client_id="H1TTOQwe_0dTr91hPRbJ-Q",
                                       client_secret="wMHrUyvnROJkTcEL93ZVGP6it-kABw",
                                       user_agent="stockbot12")

        subreddit = reddit_read_only.subreddit(pick)
        rawlst = []

        for post in subreddit.hot(limit=100):
            rawlst.append(post.title and post.selftext)
        y = (''.join([char for char in rawlst if char not in string.punctuation])).split()

        rank = {}

        for word in y:
            if word in self.stocklst:
                if word in rank:
                    rank[word] += 1
                else:
                    rank[word] = 1

        res = nlargest(3, rank, key=rank.get)
        self.first = res[0]
        self.second = res[1]
        self.third = res[2]

        print(res)


class GUI:
    def __init__(self):
        self.stocks = None

    def update_text(self):
        self.stocks.config(text= f"The top three most discussed stocks currently are {p.get_first_stock()}, {p.get_second_stock()}, {p.get_third_stock()}. \n "
                               f"Here is some info about these stocks:")

    def interface(self):
        r = tk.Tk()
        r.geometry('500x500')

        menubutton = Menubutton(r, text="File", width=35)
        menubutton.grid()
        menubutton.menu = Menu(menubutton)
        menubutton["menu"] = menubutton.menu
        menubutton.menu.add_checkbutton(label="New file", variable=IntVar())
        menubutton.menu.add_checkbutton(label="Save", variable=IntVar())
        menubutton.menu.add_checkbutton(label="Save as", variable=IntVar())
        menubutton.pack()

        instructions = Label(r, text="Select one of the following subreddits to scrape")
        wallst_button = tk.Button(r, text='r/wallstreetbets', width=15, command= lambda: [p.scrape_and_rank('wallstreetbets'), x.update_text()])
        stocks_button = tk.Button(r, text='r/stocks', width=15, command= lambda: [p.scrape_and_rank('stocks'), x.update_text()])
        stock_market_button = tk.Button(r, text='r/StockMarket', width=15, command= lambda: [p.scrape_and_rank('StockMarket'), x.update_text()])
        stock_picks_button = tk.Button(r, text='r/Stock_Picks', width=15, command= lambda: [p.scrape_and_rank('Stock_Picks'), x.update_text()])
        self.stocks = Label(r, text="")

        instructions.pack()
        wallst_button.pack()
        stocks_button.pack()
        stock_market_button.pack()
        stock_picks_button.pack()
        self.stocks.pack()
        r.mainloop()



p = back_end()
p.create_stock_list()

x = GUI()
x.interface()



#GUI does not update after three stocks are loaded
#must return links and info about stock

