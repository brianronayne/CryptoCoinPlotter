from Exchange import Binance
from Plotter import Plotter
from Indicators import Indicators
import pandas as pd
import json
import requests
import sys

def Main():
    exchange = Binance()
    print("Welcome to the coin data plotter! \n")
    print("What coin would you like to plot? \nEntries should be in the following format 'BTCUSDT', Where BTC is the base asset and USDT is the quote asset.")
    tradeableCoins = exchange.GetTradeablePairs()
    coin = input()
    if coin not in tradeableCoins:
        print("The input provided was not recognised as a coin currently tradeable on Binance. The program will now exit.")
        sys.exit(1)

    intervals = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
    
    

    print("\nWhat interval would you like to plot this coin over?")
    print("The interval may take the following values:")
    print("1m")
    print("3m")
    print("5m")
    print("15m")
    print("30m")
    print("1h")
    print("2h")
    print("4h")
    print("6h")
    print("8h")
    print("12h")
    print("1d")
    print("3d")
    print("1w")
    print("1M")     
    interval = input()
    if interval not in intervals:
        print("The input provided was not recognised as an acceptable interval value. The program will now exit.")
        sys.exit(1)

    coin_data = Binance().GetPairData(pair = coin, interval = interval)
    

    print("Choose which indicator you wish to use:")
    print("1. None")
    print("2. Bollinger Bands")
    indicator = int(input())
    if indicator == 2:
        coin_data = Indicators().BBIndicator(df = coin_data)
    Plotter().PlotPairData(coin_data)

if __name__ == "__main__":
    Main()