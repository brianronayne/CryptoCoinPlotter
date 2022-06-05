import pandas as pd
import numpy as np
from ta import add_all_ta_features
from ta.volatility import BollingerBands
from Binance import Binance

class Indicators:
    '''Class to hold trading indicators that will be used'''

    def __init__(self):
        pass

    def BBIndicator(self, df, window:int = 20, window_dev:int = 2):
        indicator_bb = BollingerBands(close=df["Close"], window=window, window_dev=window_dev, fillna=True)
        df['bb_high'] = indicator_bb.bollinger_hband()
        df['bb_low'] = indicator_bb.bollinger_lband()

        return df



def Main():
    BTCData = Binance().GetPairData(pair = "BTCUSDT")
    BB_BTC_data = Indicators().BBIndicator(df = BTCData)
    print(BB_BTC_data)


if __name__ == "__main__":
    Main()




