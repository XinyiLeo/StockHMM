# import pip
# pip.main(['install', 'pandas_datareader'])
import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
from hmmlearn.hmm import GaussianHMM

start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()

apple = web.DataReader("AAPL", "morningstar", start, end)
google = web.DataReader("GOOG", "morningstar", start, end)
microsoft = web.DataReader("MSFT", "morningstar", start, end)

# print(google["Close"].index.levels[1])

stocks = pd.DataFrame({"APPL": apple["Close"].values, "GOOG":google["Close"].values,"MSFT":microsoft["Close"].values},apple["Close"].index.levels[1])


# df = pd.DataFrame(stocks)
apple.to_csv("appledata.csv" , encoding = "utf-8")

# df2 = pd.read_csv ("testfoo.csv" , encoding = "utf-8")
# print (df2)