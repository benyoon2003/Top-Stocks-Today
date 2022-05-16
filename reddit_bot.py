import string
import praw
from heapq import nlargest
import tkinter as tk
from tkinter import *
import yfinance as yahooFinance


class back_end:
    def __init__(self):
        self.stocklst = []
        self.first = None
        self.second = None
        self.third = None
        self.first_stock_info = None
        self.second_stock_info = None
        self.third_stock_info = None
        self.userpick = None

    def get_first_stock(self):
        return self.first

    def get_second_stock(self):
        return self.second

    def get_third_stock(self):
        return self.third

    def get_first_stock_info(self):
        return self.first_stock_info

    def get_second_stock_info(self):
        return self.second_stock_info

    def get_third_stock_info(self):
        return self.third_stock_info

    def create_stock_list(self):
        with open('nasdaq') as f:
            for line in f:
                x = line.split('|')
                self.stocklst.append(x[0])

    def scrape_and_rank(self, pick):
        self.userpick = pick
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
        self.first_stock_info = yahooFinance.Ticker(self.first)
        self.second_stock_info = yahooFinance.Ticker(self.second)
        self.third_stock_info = yahooFinance.Ticker(self.third)


class GUI:
    def __init__(self):
        self.stocks = None
        self.stock1_info = None
        self.stock2_info = None
        self.stock3_info = None
        self.line1 = None
        self.line2 = None
        self.line3 = None
        self.line4 = None

    def update_text(self):
        self.stocks.config(text= f"The top three most discussed stocks on r/{p.userpick} currently are {p.get_first_stock()}, {p.get_second_stock()}, {p.get_third_stock()}. \n "
                               f"Here is some info about these stocks:")
        self.stock1_info.config(text=f"{p.get_first_stock()}/{p.get_first_stock_info().info['longName']}")
        self.line1.config(text=f"Price: {p.get_first_stock_info().info['currentPrice']}\n"
                               f"Open: {p.get_first_stock_info().info['open']}  High: {p.get_first_stock_info().info['dayHigh']}    "
                               f"Low: {p.get_first_stock_info().info['dayLow']}\n"
                               f"Mkt Cap: {p.get_first_stock_info().info['marketCap']}  Forward P/E: "
                               f"{p.get_first_stock_info().info['forwardPE']}  "
                               f"Div&Yield: {p.get_first_stock_info().info['dividendYield']}\n"
                               f"Prev. Close: {p.get_first_stock_info().info['previousClose']}  52 Wk. Low: "
                               f"{p.get_first_stock_info().info['fiftyTwoWeekLow']}  52 Wk. High: "
                               f"{p.get_first_stock_info().info['fiftyTwoWeekHigh']}\n \n"
                               f"{p.get_first_stock_info().info['longBusinessSummary']}\n\n\n", wraplength=600)
        self.stock2_info.config(text=f"{p.get_second_stock()}/{p.get_second_stock_info().info['longName']}")
        self.line2.config(text=f"Price: {p.get_second_stock_info().info['currentPrice']}\n"
                               f"Open: {p.get_second_stock_info().info['open']}  High: {p.get_second_stock_info().info['dayHigh']}    "
                               f"Low: {p.get_second_stock_info().info['dayLow']}\n"
                               f"Mkt Cap: {p.get_second_stock_info().info['marketCap']}  Forward P/E: "
                               f"{p.get_second_stock_info().info['forwardPE']}  "
                               f"Div&Yield: {p.get_second_stock_info().info['dividendYield']}\n"
                               f"Prev. Close: {p.get_second_stock_info().info['previousClose']}  52 Wk. Low: "
                               f"{p.get_second_stock_info().info['fiftyTwoWeekLow']}  52 Wk. High: "
                               f"{p.get_second_stock_info().info['fiftyTwoWeekHigh']}\n \n"
                               f"{p.get_second_stock_info().info['longBusinessSummary']}\n\n\n", wraplength=600)
        self.stock3_info.config(text=f"{p.get_third_stock()}/{p.get_third_stock_info().info['longName']}")
        self.line3.config(text=f"Price: {p.get_third_stock_info().info['currentPrice']}\n"
                               f"Open: {p.get_third_stock_info().info['open']}  High: {p.get_third_stock_info().info['dayHigh']}    "
                               f"Low: {p.get_third_stock_info().info['dayLow']}\n"
                               f"Mkt Cap: {p.get_third_stock_info().info['marketCap']}  Forward P/E: "
                               f"{p.get_third_stock_info().info['forwardPE']}  "
                               f"Div&Yield: {p.get_third_stock_info().info['dividendYield']}\n"
                               f"Prev. Close: {p.get_third_stock_info().info['previousClose']}  52 Wk. Low: "
                               f"{p.get_third_stock_info().info['fiftyTwoWeekLow']}  52 Wk. High: "
                               f"{p.get_third_stock_info().info['fiftyTwoWeekHigh']}\n \n"
                               f"{p.get_third_stock_info().info['longBusinessSummary']}", wraplength=250)


    def interface(self):
        r = tk.Tk()
        r.geometry('640x800')

        # menubutton = Menubutton(r, text="File", width=35)
        # menubutton.grid()
        # menubutton.menu = Menu(menubutton)
        # menubutton["menu"] = menubutton.menu
        # menubutton.menu.add_checkbutton(label="New file", variable=IntVar())
        # menubutton.menu.add_checkbutton(label="Save", variable=IntVar())
        # menubutton.menu.add_checkbutton(label="Save as", variable=IntVar())
        # menubutton.pack()

        instructions = Label(r, text="Select one of the following subreddits to scrape")
        wallst_button = tk.Button(r, text='r/wallstreetbets', width=15, command= lambda: [p.scrape_and_rank('wallstreetbets'), x.update_text()])
        stocks_button = tk.Button(r, text='r/stocks', width=15, command= lambda: [p.scrape_and_rank('stocks'), x.update_text()])
        stock_market_button = tk.Button(r, text='r/StockMarket', width=15, command= lambda: [p.scrape_and_rank('StockMarket'), x.update_text()])
        stock_picks_button = tk.Button(r, text='r/Stock_Picks', width=15, command= lambda: [p.scrape_and_rank('Stock_Picks'), x.update_text()])
        self.stocks = Label(r, text="")
        space = Label(r, text= "")
        self.stock1_info = Label(r, text="")
        self.stock2_info = Label(r, text="")
        self.stock3_info = Label(r, text="")
        self.line1 = Label(r, text="")
        self.line2 = Label(r, text="")
        self.line3 = Label(r, text="")
        self.line4 = Label(r, text="")

        instructions.pack()
        wallst_button.pack()
        stocks_button.pack()
        stock_market_button.pack()
        stock_picks_button.pack()
        self.stocks.pack()
        space.pack()
        self.stock1_info.pack()
        self.line1.pack()
        self.stock2_info.pack()
        self.line2.pack()
        self.stock3_info.pack()
        self.line3.pack()
        self.line4.pack()


        r.mainloop()



p = back_end()
p.create_stock_list()

x = GUI()
x.interface()



#must return background info on the company
#price per share, market cap, 52 wk high and low- can be found using
#current event articles links- these are the top 3 articles that pop up
#loading bar?

#https://thecleverprogrammer.com/2020/08/22/real-time-stock-price-with-python/