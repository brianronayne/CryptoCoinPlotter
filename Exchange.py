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

    def GetTradeablePairs(self, quote_currencies:list=['USDT', "BTC", "ETH", "EUR"]):

        '''Returns a list of all the tradeable pairs for a given quote asset'''

        url = self.base + self.endpoint['exchangeInfo']
        data= requests.get(url)
        data = json.loads(data.text)

        pairs = []

        for pair in data['symbols']:
            if pair['status'] == "TRADING" and pair['quoteAsset'] in quote_currencies:
                pairs.append(pair['symbol'])

        return pairs

    def GetPairData(self, pair:str, interval:str="1h"):

        '''
        Returns price data for a given pair on a given timeframe
        '''

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

class Coinbase():

    def __init__(self):
        self.base = "https://api.exchange.coinbase.com"
        self.endpoint = {
            "exchange_info": "/products"
        }

    def GetTradeablePairs(self, quote_currencies:list=['USDT', "BTC", "ETH", "EUR"]):
        url = self.base + self.endpoint['exchange_info']
        
        data= requests.get(url)
        data = json.loads(data.text)

        pairs = []

        for coin in data:
            if coin['trading_disabled'] == False and coin['quote_currency'] in quote_currencies:
                pairs.append(coin['id'])

        return pairs

    def GetPairData(self, pair:str, interval:str="1h"):
        url = self.base + self.endpoint['exchange_info'] + "/" + pair + "/candles"
        
        data= requests.get(url)
        data = json.loads(data.text)

        pairs = []

        for coin in data:
            if coin['trading_disabled'] == False and coin['quote_currency'] in quote_currencies:
                pairs.append(coin['id'])


        return pairs

def Main():
    exchange = Coinbase().GetTradeablePairs()
    print(exchange)

if __name__ == "__main__":
    Main()





