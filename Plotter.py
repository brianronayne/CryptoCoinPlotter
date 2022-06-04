import pandas as pd 
import plotly.graph_objects as go 
from Binance import Binance

class Plotter:
    ''' 
    Plots Candlestick Data

    '''

    def __init__(self):
        pass

    def PlotPairData(self, df):

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

def Main():
    BTCUSDT = Binance().GetPairData(pair = "BTCUSDT", interval = '1h')
    BTCUSDT.name = "BTCUSDT"
    Plotter().PlotPairData(df = BTCUSDT)

if __name__ == "__main__":
    Main()