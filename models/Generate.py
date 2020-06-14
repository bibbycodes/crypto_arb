from models.Validate import Validate
from models.Trade import Trade
from models.Parse import Parse

class Generate:
  @staticmethod
  def sequence(sequential_coins, markets, tickers, is_trade):
    trades_array = []
    for i, from_coin in enumerate(sequential_coins):
      if i == len(sequential_coins) - 1:
        to_coin = sequential_coins[0]
      else:
        to_coin = sequential_coins[i + 1]
    
      trade = Validate.correct_pair(markets, from_coin, to_coin)

      if trade:
        trade = Parse.trade(trade, from_coin, to_coin)
        if is_trade:
          trade_instance = Trade(trade, tickers)  
          trades_array.append(trade_instance)
        else:
          trades_array.append(trade['symbol'])
      else:
        return False

    return trades_array

  @staticmethod
  def sequential_trades(sequential_coins, markets, tickers):
    trades_array = []
    for i, coin in enumerate(sequential_coins):
      from_coin = sequential_coins[i]

      if i == len(sequential_coins) - 1:
        to_coin = sequential_coins[0]
      else:
        to_coin = sequential_coins[i + 1]
      trade = Validate.correct_pair(markets, from_coin, to_coin)

      if trade != False:
        trade = Parse.trade(trade, from_coin, to_coin)
        trade_instance = Trade(trade, tickers)
        trades_array.append(trade_instance)

    if False in trades_array:
      return False

    return trades_array


  @staticmethod
  def sequential_symbols(sequential_coins, markets):
    trades_array = []
    for i in range(len(sequential_coins)):
      from_coin = sequential_coins[i]

      if i == len(sequential_coins) - 1:
        to_coin = sequential_coins[0]
      else:
        to_coin = sequential_coins[i + 1]
        
      trade = Validate.correct_pair(markets, from_coin, to_coin)
      
      if(trade):
        trades_array.append(trade['symbol'])
      else:
        trades_array.append(False)

    if None in trades_array:
      return False

    return trades_array




