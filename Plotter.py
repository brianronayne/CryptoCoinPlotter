import pandas as pd 
import plotly.graph_objects as go 
from Binance import Binance

class Plotter:
    ''' 
    Class for controlling all plotting
    '''

    def __init__(self):
        pass

    def PlotPairData(self, df):
        '''
        Given a dataframe containing price data for a pair, will create a candlestick plot.
        '''

        data = go.Candlestick(
            x = df['Time'],
            open = df['Open'],
            high = df['High'],
            low = df['Low'],
            close = df['Close']
            )

        fig = go.Figure(data = [data])
        fig.update_layout(title = df.name)

        fig.show()