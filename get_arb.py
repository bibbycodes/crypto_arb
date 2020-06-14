from models.Generate import Generate
from models.Format import Format 
from models.Arb import Arb
import ccxt
import asyncio
import json
from pgdb import connect
import itertools

hostname = 'localhost'
username = 'bibbycodes'
database = 'crypto_arb'

dbConn = connect(host=hostname, user=username, dbname=database)
cursor = dbConn.cursor()

def filter_tickers(tickers):
  filtered = {}
  for k,v in tickers.items():
    if tickers[k]['bid'] == 0.0 or tickers[k]['ask'] == 0.0:
      pass
    else:
      filtered[k] = v
  # print(filtered)
  return filtered

def get_arbs(exchange_name, markets, set_of_combinations):
  list_of_coin_sequences = []
  array_of_sequential_trade_symbols = []

  for combination in set_of_combinations:
    trade_symbols = Generate.sequential_symbols(combination, markets)
    if trade_symbols is not None:
      list_of_coin_sequences.append(combination)
      array_of_sequential_trade_symbols.append(trade_symbols)
      
  set_of_symbols = [item for sublist in array_of_sequential_trade_symbols for item in sublist]
  tickers = exchange.fetch_tickers(set_of_symbols)
  filtered_tickers = filter_tickers(tickers)
  print(filtered_tickers.keys())
  # list_of_trade_sequences = [Generate.sequential_trades(coin_set, markets, filtered_tickers) for coin_set in list_of_coin_sequences]

  # for trade_sequence in list_of_trade_sequences:
  #   arb_object = Arb(trade_sequence)
  #   db_string = Format.db_arb_string(arb_object, exchange_name)
  #   print(db_string)
  #   ex = cursor.execute(db_string)



  dbConn.commit()
  cursor.close()


exchange = getattr(ccxt, 'binance')()
markets = exchange.load_markets()

cryptos = ['ETH', 'BTC', 'XRP', 'BCH', 'LTC', 'BNB', 'EOS', 'XZT', 'LINK', 'XMR', 'XLM', 'ADA', 'TRX', 'DASH', 'ETC', 'ALGO', 'NEO', 'ATOM', 'IOTA', 'XEM', 'ONT', 'FFT', 'DOGE', 'ZEC']
combinations = list(itertools.combinations(cryptos, 4))
get_arbs(exchange.name.lower(), markets, [['EUR', 'BTC', 'NGN', 'BNB'], ['USDT', 'BTC', 'ETH', 'BNB']] + combinations)
