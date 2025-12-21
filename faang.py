#! /usr/bin/env python
#https://realpython.com/python-shebang/


# The above shebang should be put on the first line above any imports(must be done like that)
# This put at the top is to say this script should be run in python, and maes the file exacutable


# followed by the imports

import datetime as dt

import pandas as pd

import yfinance as yf

import numpy as np

import matplotlib.pyplot as plt


# followed by the downloading of data needed
Tickers = yf.Tickers('META AAPL GOOG AMZN NFLX')

df = yf.download(['META', 'AAPL', 'GOOG', 'AMZN', 'NFLX'], period='5d', interval='1h')

# filename and datetime setup

df.to_csv("data/" + dt.datetime.now().strftime("%Y%m%d %H%M%S") + ".csv")



# plotting the close data
df[[('Close', 'META'), ('Close', 'AAPL'), ('Close', 'GOOG'), ('Close', 'AMZN'), ('Close', 'NFLX')]].plot()

df['Close'].plot()



fig, ax = plt.subplots()

df['Close'].plot(ax=ax)

# current date and time 
now = dt.datetime.now()

#filename based on timestamp,change place and type
filename = "plots/" + dt.datetime.now().strftime("%Y%m%d %H%M%S") + ".png"


#save to folder and make the pixels better quality
fig.savefig(filename, dpi=300)


# in terminal must use chmod +x faang.py
# this gives the file permission to execute or check if it is ls -l ,which gives everything in folder in long list with more info
#can be seen there

# references in problems notebook
# ://realpython.com/python-shebang/
