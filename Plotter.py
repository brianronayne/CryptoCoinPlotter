import pandas as pd 
import plotly.graph_objects as go 
from Binance import Binance
import datetime

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

        candlestick = go.Candlestick(
            x = df['Time'],
            open = df['Open'],
            high = df['High'],
            low = df['Low'],
            close = df['Close'],
            name = "Price Data"
            )
        data = [candlestick]

        if "bb_low" in df.columns:
            bb_low_data =  go.Scatter(
            x = df['Time'],
            y = df['bb_low'],
            name = "Lower Bollinger Band",
            line = dict(color = (' rgba(55,118,171,1.00)'))
            )

            data.append(bb_low_data)

        if "bb_high" in df.columns:
            bb_high_data =  go.Scatter(
            x = df['Time'],
            y = df['bb_high'],
            name = "Upper Bollinger Band", 
            line = dict(color = (' rgba(55,118,171,1.00)'))
            )

            data.append(bb_high_data)

        fig = go.Figure(data = data)
        fig.update_layout(title = df.name,xaxis_rangeslider_visible = False)

        # fig.write_image("graphs/" + df.name + "-"+str(datetime.datetime.now())+".jpeg")
        fig.write_image("C:/Users/Brian Ronayne/Desktop/Programming/CryptoCoinPlotter/graphs/fig1.jpeg")

        fig.show()