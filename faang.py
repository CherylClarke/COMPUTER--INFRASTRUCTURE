#! /usr/bin/env python



# dates and times
import datetime as dt


# data frame , pulled in with yfinance anyway 
import pandas as pd

# import yahoo finance data
import yfinance as yf

# used in problem 2.
# numerical arrays
import numpy as np

#plotting
import matplotlib.pyplot as plt


Tickers = yf.Tickers('META AAPL GOOG AMZN NFLX')

df = yf.download(['META', 'AAPL', 'GOOG', 'AMZN', 'NFLX'], period='5d', interval='1h')

df.to_csv("data/" + dt.datetime.now().strftime("%Y%m%d %H%M%S") + ".csv")

df[[('Close', 'META'), ('Close', 'AAPL'), ('Close', 'GOOG'), ('Close', 'AMZN'), ('Close', 'NFLX')]].plot()

df['Close'].plot()

# create new figure and axis
# ax tell what the arguement is and subplot creates a blank plot
fig, ax = plt.subplots()

# plot all closing prices
# insert the arguements
df['Close'].plot(ax=ax)

# current date and time (getting current time stamp)(as used above)
now = dt.datetime.now()

# file name (creating a new filename based on new timestamp)(as used above)(change place(plot) and change type to (png)
filename = "plots/" + dt.datetime.now().strftime("%Y%m%d %H%M%S") + ".png"


# save figure to plots folder
# dpi is the pixels per inch , from lecture found that 300 is suitable amount for it to not look blocky
fig.savefig(filename, dpi=300)