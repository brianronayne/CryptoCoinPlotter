import pandas as pd 
import json
import requests

class Binance():
    '''
    Will control all interactions with the the binance API
    '''

    def __init__(self):
        self.base = "https://api.binance.com"

        self.endpoint = {
            "exchangeInfo": "/api/v3/exchangeInfo",
            "candlestick": "/api/v3/klines"
        }

    def getTradeablePairs(self, quoteCurrencies:list=['USDT', "BTC", "ETH", "EUR"]):
        url = self.base + self.endpoint['exchangeInfo']
        data= requests.get(url)
        data = json.loads(data.text)

        pairs = []

        for pair in data['symbols']:
            if pair['status'] == "TRADING" and pair['quoteAsset'] in quoteCurrencies:
                pairs.append(pair['symbol'])

        return pairs

    def GetPairData(self, pair, interval):
        url = self.base + self.endpoint['candlestick'] + "?&symbol=" + pair + "&interval=" + interval

        data = requests.get(url)

        dataJson = json.loads(data.text)

        df = pd.DataFrame.from_dict(dataJson)

        df = df.drop(11, axis = 1)

        colNames = ["Time", "Open", "High", "Low", "Close", "Volume", 'Close Time', 'Quote Asset Volume', 
        'Number of Trades', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume'] 

        df.columns = colNames

        df["Time"] = pd.to_datetime(df['Time'],unit='ms')

        for col in colNames[1:]:
            df[col] = df[col].astype(float)

        df.name = pair

        return df

def Main():
    exchange = Binance()
    symbols = exchange.getTradeablePairs()
    print(symbols)
    print(exchange.getPairData(pair = symbols[0], interval = '1m'))

if __name__ == "__main__":
    Main()