from queue import Queue


TOTAL_EQUITY = 10000
equity_center = dict()
datacenter = dict()

TIME_RANGE, PRICE_RANGE = 40, 40
MAX_DATA_LENGTH = 200
if MAX_DATA_LENGTH < TIME_RANGE:
    MAX_DATA_LENGTH = TIME_RANGE

stocks = ['TSLA']


database = Queue()


am_stocks = []
for i in range(len(stocks)):
    am_stocks.append(f"AM.{stocks[i]}")
