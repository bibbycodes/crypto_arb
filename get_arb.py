from models.Generate import Generate
from models.Format import Format 
from models.Arb import Arb
import ccxt
import asyncio
import json
from pgdb import connect
import itertools
import json

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
  return filtered

def get_coin_list(tickers):
  coins = []
  for symbol, ticker in tickers.items():
    coin_a, coin_b = symbol.split('/')
    coins.append(coin_a)
    coins.append(coin_b)

  return coins
    

def save_generated_trades(exchange_name, markets, tickers, length):
  filtered_tickers = filter_tickers(tickers)
  list_of_coin_sequences = []
  array_of_sequential_trade_symbols = []
  set_of_coins = set(get_coin_list(filtered_tickers))
  set_of_combinations = list(itertools.combinations(set_of_coins, length))
  print(f"got combos {exchange_name} - length: {length}")

  for combination in set_of_combinations:
    trade_symbols = Generate.sequential_symbols(combination, filtered_tickers)
    if trade_symbols != False and False not in trade_symbols:
      list_of_coin_sequences.append(combination)
      array_of_sequential_trade_symbols.append(trade_symbols)

  print("Got sequences")

  print("Saving File: ", f'json/locs_of_len_{length}-{exchange_name}.json')
  with open(f'json/locs_of_len_{length}-{exchange_name}.json', 'w') as outfile:
    json.dump(list_of_coin_sequences, outfile)

  print("Saving File: ", f'json/asts_of_len_{length}-{exchange_name}.json')
  with open(f'json/asts_of_len_{length}-{exchange_name}.json', 'w') as outfile:
    json.dump(array_of_sequential_trade_symbols, outfile)
      
  # set_of_symbols = [item for sublist in array_of_sequential_trade_symbols for item in sublist]
  # print(set_of_symbols)
  # list_of_trade_sequences = [Generate.sequential_trades(coin_set, markets, filtered_tickers) for coin_set in list_of_coin_sequences]

  # for trade_sequence in list_of_trade_sequences:
  #   arb_object = Arb(trade_sequence)
  #   db_string = Format.db_arb_string(arb_object, exchange_name)
  #   print(db_string)
  #   ex = cursor.execute(db_string)

def get_arbs_from_file(markets, filtered_tickers, exchange_name):
  with open('array_of_sequential_trade_symbol.json') as f:
    trades_data = json.load(f)
    with open('list_of_coin_sequences.json') as g:
      coin_data = json.load(g)
      array_of_sequential_trade_symbols = trades_data[0]
      list_of_coin_sequences = coin_data
      print("Flattening set of symbols")
      set_of_symbols = [item for sublist in array_of_sequential_trade_symbols for item in sublist]
      list_of_trade_sequences = [Generate.sequential_trades(coin_set, markets, filtered_tickers) for coin_set in list_of_coin_sequences]
      for trade_sequence in list_of_trade_sequences:
        if trade_sequence:
          arb_object = Arb(trade_sequence)
          db_string = Format.db_arb_string(arb_object, exchange_name)
          ex = cursor.execute(db_string)
  
exchanges = ccxt.exchanges

for ex in exchanges:
  try:
    exchange = getattr(ccxt, ex)()
    if exchange.has['fetchTickers'] and exchange.has['loadMarkets']:
      if exchange.has['publicAPI']:
          tickers = exchange.fetch_tickers()
          markets = exchange.load_markets()
          save_generated_trades(exchange.name.lower(), markets, tickers, 4)
  except Exception:
    pass

  



# cryptos = ['ETH', 'BTC', 'XRP', 'BCH', 'LTC', 'BNB', 'EOS', 'XZT', 'LINK', 'XMR', 'XLM', 'ADA', 'TRX', 'DASH', 'ETC', 'ALGO', 'NEO', 'ATOM', 'IOTA', 'XEM', 'ONT', 'FFT', 'DOGE', 'ZEC']
# combinations = list(itertools.combinations(cryptos, 4))
# get_arbs(exchange.name.lower(), markets, combinations, filtered_tickers)
# get_arbs_from_file(markets, tickers, exchange.name.lower())
# dbConn.commit()
# cursor.close()
