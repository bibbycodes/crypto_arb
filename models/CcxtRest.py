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

print(CcxtRest.order_book('binance', 'ETH/USDT'))