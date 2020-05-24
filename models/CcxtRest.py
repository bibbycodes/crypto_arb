import ccxt
from time import time

class CcxtRest:
  @staticmethod
  def order_book(ex, pair):
    try:
      exchange = getattr(ccxt, ex)()
      markets = exchange.load_markets()
      if (markets[pair]):
        order_book = exchange.fetch_order_book(pair)
        timestamp = timestamp = int(time()*1000.0)

        return {
          "timestamp" : timestamp,
          "exchange": ex,
          "pair" : pair,
          "ask" : order_book["asks"][0][0],
          "ask_volume" : order_book["asks"][0][1],
          "bid" : order_book["bids"][0][0],
          "bid_volume" : order_book["bids"][0][1]
        }
    except Exception as e:
      raise

  @staticmethod
  def ticker(ex, pair):
    exchange = getattr(ccxt, ex)()
    ticker = exchange.fetch_ticker(pair)
    return {
      "exchange" : ex,
      "pair" : pair,
      "ask" : ticker["ask"],
      "bid" : ticker["bid"],
      "last" : ticker["last"],
      "open" : ticker["open"],
      "close" : ticker["close"],
      "timestamp" : ticker["timestamp"]
    }

print(CcxtRest.ticker("binance", "BTC/USDT"))