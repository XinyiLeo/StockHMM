## Introduction
I finally finish one of my dream this year to play with some codes in stock indexes estimation. In January to Martch I made some literature research for a wide-used hidden markov - stochastic volatility models, see [Literature Research](https://github.com/XinyiLeo/Samples/blob/master/Xinyi%20Wu_433%20final%20report.pdf). Later in Machine learning course, I used software like Weka to give some baseline predictions and finally understood and revised some codes in HMM stock prediction. This is my first ML project in finance. Regard it as prototype, because it is far from mature to put in to reality algo trading. 

## Background
I myself ﬁrmly believe that algorithms is the core backbone of trading strategy, despite that human operations like legal policies and government regulation can push the stock up and down some time. The essence and charisma of machine learning algorithms will apparently stand out in high frequency trading (HFT). HFT aims to do quantitative trading by designing algorithm to buy or sell a product in a very transient time period that mostly cannot be realized by human beings. The proﬁt of a buy/sell is very little, but we do millions of trading within a day. So the proﬁt summed up is observable.

I used python3 to implemet codes and visualize data. I revised some codes in HMM. Those codes are for education purpose, but I revised them in my financial projects. My revised codes are here [My codes]. 

## Visualization for historical data
Those are visualization of three close values: Apple Inc. (NASDAQ:AAPL), Microsoft (NASDAQ:MSFT) and Google (NASDAQ:GOOG), from 2016 January to 2018 June. 
![Apple Close Value](https://github.com/XinyiLeo/StockHMM/blob/master/graphs/graph4.png)

I extracted data from Morningstar Investment management company, because it has high compatibility with pandas in python. The current inputs are extracted from historical ﬁnancial time series data, which includes: 
1. Daily Open: the price of the stock at the beginning of the trading day (it need not be the closing price of the previous trading day).
2. Daily High: the highest price of the stock on that trading day.
3. Daily Low: the lowest price of the stock on that trading day, and close the price of the stock at closing time.
4. Adjusted close: the closing price of the stock that adjusts the price of the stock for corporate actions.

A good way to visualize all data is by Candlestick Chart. In this chart. If the daily open value is lower than the close value, the bar is black (reported a gain). If the daily close value is higher than the open value, the bar is red (reported a loss). The wicks on the top and lower part of the bar means the high value and low value of a day.  
![Candle Stick](https://github.com/XinyiLeo/StockHMM/blob/master/graphs/graph3.png)

In finance, we concerned about the relative change of an asset rather than its absolute price. That’s because when we trade, we concern more about the volatility of a stock price.

<img src="https://latex.codecogs.com/gif.latex?return_{t,0}&space;=&space;\dfrac{price_t}{price_0}" title="return_{t,0} = \dfrac{price_t}{price_0}" />

![Return](https://github.com/XinyiLeo/StockHMM/blob/master/graphs/graph5.png)

Log return is a much more useful plot. We can now see how profitable each stock was since the beginning of the period. Furthermore, we see that these stocks are highly correlated; they generally move in the same direction, a fact that was difficult to see in the other charts. 

![Return](https://github.com/XinyiLeo/StockHMM/blob/master/graphs/graph6.png)

Another possible feature for stock estimation is Moving Average,  
<a href="https://www.codecogs.com/eqnedit.php?latex=MA_t^q&space;=&space;\dfrac{1}{q}&space;\sum\limits_{i=0}^{q-1}&space;x_{t-i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?MA_t^q&space;=&space;\dfrac{1}{q}&space;\sum\limits_{i=0}^{q-1}&space;x_{t-i}" title="MA_t^q = \dfrac{1}{q} \sum\limits_{i=0}^{q-1} x_{t-i}" /></a>

Moving averages smooth a series and helps identify trends, and help identify trends from “noise”. 

![Return](https://github.com/XinyiLeo/StockHMM/blob/master/graphs/graph7.png)

Here, the 200-day moving average shows that the stock is trending downward over ina general view. 
Also the crossing of moving average lines indicate changes in trend, which can be used as trading signals, or indications that a financial security is changing direction and a profitable trade might be made.

![Return](https://github.com/XinyiLeo/StockHMM/blob/master/graphs/graph8.png)













