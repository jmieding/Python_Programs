"""
Python 2.7.10

Puzzle: Find the most profitable trade possible given a list where each 
index represents a minute of the day, and the item at each index is the 
value of the stock price. Shorting stock is not allowed.
"""

stock_price = [500, 501, 502, 499, 480, 510, 480]
best_trade = [(0, 0, 0)]

for buy in stock_price:
  sell = max(stock_price[stock_price.index(buy):])
  if sell - buy > best_trade[0][-1]:
    best_trade[0] = (buy, sell, int(sell - buy))
  else:
    pass
print best_trade


""""
Note that having duplicate items in the list doesn't affect the program.
While the max() method will always be called with reference to the earliest 
occurence of a duplicate list item (because of the index() method), calling
the max() method with reference to later occurrences of the item would only 
result in a lower or equal best_trade.

For example: if l = [500, 600, 500, 400], calling max() on 500 at [2] would 
result in a loss, and if l = [500, 600, 500, 700], calling max() on 500 at [2]
would result in an equivalent answer to calling max on 500 at [0].
"""