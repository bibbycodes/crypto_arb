import models.Validate
import models.Trade

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
