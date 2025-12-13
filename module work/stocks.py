

# dates and times
import datetime as dt

# yahoo finance data
import yfinance as yf

# get the data 
df = yf.download(['AAPL', 'MSFT', 'GOOG'], period='5d', interval='1h')

# current date and time 

now = dt.datetime.now()
