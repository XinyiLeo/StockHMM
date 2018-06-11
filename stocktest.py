#  ref https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/
import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
import matplotlib.dates as mtd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from mpl_finance import candlestick_ohlc
import numpy as np

start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()

apple = web.DataReader("AAPL", "morningstar", start, end)
type(apple)
apple.head()

# Visualize the data
# apple["Close"].plot(grid=True)
# plt.show()

# Candlestick chart
def pandas_candlestick_ohlc(dat, stick = "day", otherseries = None):
    # This will show a Japanese candlestick plot for stock data stored in dat, also plotting other series if passed.
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    dayFormatter = DateFormatter('%d')      # e.g., 12

    # Create a new DataFrame which includes OHLC data for each period specified by stick input
    transdat = dat.loc[:,["Open", "High", "Low", "Close"]]
    if (type(stick) == str):
        if stick == "day":
            plotdat = transdat
            stick = 1  # Used for plotting
        elif stick in ["week", "month", "year"]:
            if stick == "week":
                transdat["week"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[1])  # Identify weeks
            elif stick == "month":
                transdat["month"] = pd.to_datetime(transdat.index).map(lambda x: x.month)  # Identify months
            transdat["year"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[0])  # Identify years
            grouped = transdat.groupby(list(set(["year", stick])))  # Group by year and other appropriate variable
            plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [],
                                    "Close": []})  # Create empty data frame containing what will be plotted
            for name, group in grouped:
                plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                       "High": max(group.High),
                                                       "Low": min(group.Low),
                                                       "Close": group.iloc[-1, 3]},
                                                      index=[group.index[0]]))
            if stick == "week":
                stick = 5
            elif stick == "month":
                stick = 30
            elif stick == "year":
                stick = 365
    elif (type(stick) == int and stick >= 1):
        transdat["stick"] = [np.floor(i / stick) for i in range(len(transdat.index))]
        grouped = transdat.groupby("stick")
        plotdat = pd.DataFrame(
            {"Open": [], "High": [], "Low": [], "Close": []})  # Create empty data frame containing what will be plotted
        for name, group in grouped:
            plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                   "High": max(group.High),
                                                   "Low": min(group.Low),
                                                   "Close": group.iloc[-1, 3]},
                                                  index=[group.index[0]]))
    else:
        raise ValueError(
            'Valid inputs to argument "stick" include the strings "day", "week", "month", "year", or a positive integer')

        # Set plot parameters, including the axis object ax used for plotting
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    if (plotdat.index[-1][1] - plotdat.index[0][1]) < pd.Timedelta('730 days'):
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
    else:
        weekFormatter = DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(weekFormatter)

    ax.grid(True)

    # Create the candelstick chart
    tmplist = []
    for i in plotdat.index.tolist():
        tmplist.append(i[1])
    candlestick_ohlc(ax, list(
        zip(list(mtd.date2num(tmplist)), plotdat["Open"].tolist(), plotdat["High"].tolist(),
            plotdat["Low"].tolist(), plotdat["Close"].tolist())),
                     colorup="black", colordown="red", width=stick * .4)

    # Plot other series (such as moving averages) as lines
    if otherseries != None:
        if type(otherseries) != list:
            otherseries = [otherseries]
        # I revise here
        for inp in otherseries:
            tmpvalue = []
            for i in dat.loc[:, [inp]].values:
                tmpvalue.append(i[0])
            tmppp = pd.DataFrame(
                {inp: tmpvalue},
                dat.loc[:, [inp]].index.levels[1])
            tmppp.plot(ax=ax, lw=1.3, grid=True)

    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()

# pandas_candlestick_ohlc(apple)
start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()

google = web.DataReader("GOOG", "morningstar", start, end)
microsoft = web.DataReader("MSFT", "morningstar", start, end)

# Below I create a DataFrame consisting of the adjusted closing price of these stocks,
# first by making a list of these objects and using the join method
stocks = pd.DataFrame({"AAPL": apple["Close"],
                      "MSFT": microsoft["Close"],
                      "GOOG": google["Close"]})
# stocks = pd.DataFrame({"GOOG":google["Close"].values,"MSFT":microsoft["Close"].values, "APPL": apple["Close"].values},google["Close"].index.levels[1])
print(stocks.head())
stocks.plot(grid = True)
plt.show()

# stocks.plot(secondary_y = ["AAPL", "MSFT"], grid = True)
# plt.show()

# df.apply(arg) will apply the function arg to each column in df, and return a DataFrame with the result
# Recall that lambda x is an anonymous function accepting parameter x; in this case, x will be a pandas Series object
# stock_return = stocks.apply(lambda x: x / x[0])
# stock_return.head()
# stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
# plt.show()

# Let's use NumPy's log function, though math's log function would work just as well
# stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1)))  # shift moves dates back by 1.
# stock_change.plot(grid = True).axhline(y = 0, color = "black", lw = 2)
# plt.show()

# Apple Candle
# start = datetime.datetime(2018, 1, 1)
# end = datetime.date.today()
# apple = web.DataReader("AAPL", "morningstar", start, end)
# apple["20d"] = np.round(apple["Close"].rolling(window = 20, center = False).mean(), 2)
# # pandas_candlestick_ohlc(apple, otherseries = "20d")
#
#
# start = datetime.datetime(2016, 1, 1)
# end = datetime.date.today()
# apple = web.DataReader("AAPL", "morningstar", start, end)
#
# apple["20d"] = np.round(apple["Close"].rolling(window = 20, center = False).mean(), 2)
# apple["50d"] = np.round(apple["Close"].rolling(window = 50, center = False).mean(), 2)
# apple["200d"] = np.round(apple["Close"].rolling(window = 200, center = False).mean(), 2)
#
# pandas_candlestick_ohlc(apple, otherseries = ["20d", "50d", "200d"])