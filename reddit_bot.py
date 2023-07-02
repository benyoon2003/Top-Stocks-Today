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
        """Opens the txt file of all public companies listed on the NASDAQ
        :return: a list of all the stock abbreviations
        """
        with open('nasdaq') as f:
            for line in f:
                x = line.split('|')
                self.stocklst.append(x[0])

    def scrape_and_rank(self, pick):
        """Scrapes the selected subreddit and counts the number of times a stock abbreviation is mentioned
        :param pick: a string
        :return: first, second, and third most discussed stocks
        """
        # Creates PRAW instance
        self.userpick = pick
        reddit_read_only = praw.Reddit(client_id="H1TTOQwe_0dTr91hPRbJ-Q",
                                       client_secret="wMHrUyvnROJkTcEL93ZVGP6it-kABw",
                                       user_agent="stockbot12")
        subreddit = reddit_read_only.subreddit(pick)
        rawlst = []

        # Scrapes subreddit
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
        # Pulls stock info from yahoo finance
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
        """Updates the text on the GUI when a subreddit is selected"""
        self.stocks.config(text= f"The top three most discussed stocks on r/{p.userpick} currently are {p.get_first_stock()}, "
                                 f"{p.get_second_stock()}, {p.get_third_stock()}. \n "
                               f"Here is some info about these stocks:")
        # Configures tkinter labels to show stock info from yahoo finance
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
                               f"{p.get_first_stock_info().info['longBusinessSummary']}\n\n", wraplength=1500)
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
                               f"{p.get_second_stock_info().info['longBusinessSummary']}\n\n", wraplength=1500)
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
                               f"{p.get_third_stock_info().info['longBusinessSummary']}", wraplength=1500)

    def interface(self):
        """Initializes tkinter buttons and labels"""
        r = tk.Tk()
        r.geometry('1920x1080')
        r.title('Top Stocks')
        instructions = Label(r, text="Select one of the following subreddits to scrape")
        wallst_button = tk.Button(r, text='r/wallstreetbets', width=15, command= lambda: [p.scrape_and_rank('wallstreetbets'),
                                                                                          x.update_text()], bg= 'gray')
        stocks_button = tk.Button(r, text='r/stocks', width=15, command= lambda: [p.scrape_and_rank('stocks'), x.update_text()],
                                  bg= 'gray')
        stock_market_button = tk.Button(r, text='r/StockMarket', width=15, command= lambda: [p.scrape_and_rank('StockMarket'),
                                                                                             x.update_text()], bg= 'gray')
        stock_picks_button = tk.Button(r, text='r/Stock_Picks', width=15, command= lambda: [p.scrape_and_rank('Stock_Picks'),
                                                                                            x.update_text()], bg= 'gray')
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

