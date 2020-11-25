import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web


def get_adj_close(ticker, start, end):
    '''
    :param ticker: equity label.
    :param start: start date.
    :param end: end date.
    :return: pandas dataframe of closed prices.
    '''
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)


if __name__ == "__main__":
    # Yahoo Finance Query
    tsco = get_adj_close('TSCO.L', '01/01/2020', '25/11/2020')
    # 30 day MA and STD
    tsco['30 day MA'] = tsco['Adj Close'].rolling(window=20).mean()
    tsco['30 day STD'] = tsco['Adj Close'].rolling(window=20).std()
    # Upper and Lower Bands
    tsco['Upper Band'] = tsco['30 day MA'] + (tsco['30 day STD'] * 2)
    tsco['Lower Band'] = tsco['30 day MA'] - (tsco['30 day STD'] * 2)

    plt.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    # Index values for the X axis
    x_axis = tsco.index.get_level_values(0)

    # Plot shading
    ax.fill_between(x_axis, tsco['Upper Band'], tsco['Lower Band'], color='grey')

    # Plot Adjusted Closing Price and MA
    ax.plot(x_axis, tsco['Adj Close'], color='blue', lw=2, label='Adj Close')
    ax.plot(x_axis, tsco['30 day MA'], color='black', lw=2, label='30 day MA')

    # Set Title & Show the Image
    ax.set_title('30 Day Bollinger Band for Tesco')
    ax.set_xlabel('Date (Year/Month)')
    ax.set_ylabel('Price(GBP)')
    ax.legend()
    plt.show()