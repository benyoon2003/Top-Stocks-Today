import string
import praw
from heapq import nlargest


user = int(input('Enter what subreddit you would like to scrape: \n'
             '1: wallstreetbets \n'
             '2: stocks \n'
             '3: StockMarket \n'
             '4: Stock_Picks \n'))
if user == 1:
    pick = 'wallstreetbets'
if user == 2:
    pick = 'stocks'
if user == 3:
    pick = 'StockMarket'
if user == 4:
    pick = 'Stock_Picks'

stocklst = []
with open('nasdaq') as f:
    for line in f:
        x = line.split('|')
        stocklst.append(x[0])


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
    if word in stocklst:
        if word in rank:
            rank[word] += 1
        else:
            rank[word] = 1

for stock, count in rank.items():
    print(stock, count)

res = nlargest(3, rank, key = rank.get)
print(res)


#so far program return three most mentioned stocks mentioned in wallstreet bets by stock abbreviation
#must turn everything into classes, create GUI, and return links and info about stock









