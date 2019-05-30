import pandas as pd
import quandl
import datetime
import matplotlib.pyplot as plt
import numpy as np
import candlestick

quandl.ApiConfig.api_key = ""
# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
s = "AAPL"
apple = quandl.get("WIKI/" + s, start_date=start, end_date=end)

type(apple)

print(apple.head())


#RANDOM
#plt.close('all')
#ts = pd.Series(np.random.randn(1000),
#index=pd.date_range('1/1/2000', periods=1000))
#ts = ts.cumsum()
#ts.plot()


# This line is necessary for the plot to appear in a Jupyter notebook
#%matplotlib inline
# Control the default size of figures in this Jupyter notebook
# %pylab inline
#pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots
 
apple["Adj. Close"].plot(grid = True) # Plot the adjusted closing price of AAPL

plt.show()

candlestick.pandas_candlestick_ohlc(apple, adj=True, stick="month")