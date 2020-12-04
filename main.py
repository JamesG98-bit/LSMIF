import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as web

#TODO: Complete RSI Analysis.
#TODO: Analyse object model.
#TODO: Present to LSMIF.
#TODO: Prepare to incorporate into web application.


class Equity:

    def __init__(self, name, end, start):
        self.ticker = name
        self.end = end
        self.start = start
        self.df = web.DataReader(self.ticker, data_source='yahoo', start=self.start, end=self.end)['Adj Close']

    def bb(self):

        df = pd.DataFrame(self.df)

        df['30 day MA'] = df['Adj Close'].rolling(window=20).mean()
        df['30 day STD'] = df['Adj Close'].rolling(window=20).std()
        # Upper and Lower Bands
        df['Upper Band'] = df['30 day MA'] + (df['30 day STD'] * 2)
        df['Lower Band'] = df['30 day MA'] - (df['30 day STD'] * 2)

        plt.style.use('fivethirtyeight')
        fig = plt.figure(figsize=(12, 6))

        ax = fig.add_subplot(111)

        x_axis = df.index.get_level_values(0)

        ax.fill_between(x_axis, df['Upper Band'], df['Lower Band'], color='grey')

        # Plot Adjusted Closing Price and MA
        ax.plot(x_axis, df['Adj Close'], color='blue', lw=2, label='Adj Close')
        ax.plot(x_axis, df['30 day MA'], color='black', lw=2, label='30 day MA')

        # Set Title & Show the Image
        ax.set_title(f'30 Day Bollinger Band for {self.ticker.upper()}')
        ax.set_xlabel('Date (Year/Month)')
        ax.set_ylabel('Price(GBP)')
        ax.legend()

    def rsi(self):

        df = pd.DataFrame(self.df)
        df['CHANGE'] = df['Adj Close'].diff()

        '''fig = plt.figure()
        fig.set_size_inches((25, 18))
        ax_rsi = fig.add_axes((0, 0.24, 1, 0.2))
        ax_rsi.plt(df.index, [70] * len(df.index), label="overbought")
        ax_rsi.plot(df.index, [30] * len(df.index), label='oversold')
        ax_rsi.plot(df.index, rsi, label="rsi")
        ax_rsi.plot(df["Close"])
        ax_rsi.legend()'''


if __name__ == "__main__":

    ticker = input('Please enter a ticker... ')
    end_date = dt.datetime.now()
    start_date = end_date.replace(year=end_date.year - 1)

    for date in (start_date, end_date):
        date.strftime("%d/%m/%Y")

    Object = Equity(ticker, end_date, start_date)
    Object.rsi()