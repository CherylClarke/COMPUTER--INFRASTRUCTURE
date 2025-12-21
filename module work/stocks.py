
#! /usr/bin/env python


# dates and times
import datetime as dt

# yahoo finance data
import yfinance as yf

# get the data (downloding the data)
df = yf.download(['AAPL', 'MSFT', 'GOOG'], period='5d', interval='1h')

# current date and time (getting current time stamp)
now = dt.datetime.now()

# file name (creating a new filename based on new timestamp)
filename = "../data/" + dt.datetime.now().strftime("%Y%m%d %H%M%S") + ".csv"

#save data as csv (saving the new filename)
df.to_csv(filename)



