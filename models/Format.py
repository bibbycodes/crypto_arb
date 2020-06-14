from time import time

class Format:
  @staticmethod
  def ticker_object(price, pair, exchange, base, quote, converter):
    return {
      "price": price,
      "pair": pair,
      "exchange": exchange,
      "base": base,
      "quote": quote,
      "converter": converter
    }

  @staticmethod
  def db_arb_string(arb_obj, exchange):
    coins = []
    asks = []
    bids = []
    pairs = []
    outcomes = arb_obj.outcomes
    timestamp = timestamp = int(time()*1000.0)

    columns = [
      'timestamp', 'exchange', 'arb_rate',
      'coin_1', 'coin_2', 'coin_3', 'coin_4', 
      'trade_1_ask', 'trade_1_bid', 'trade_1_pair', 'outcome_1',
      'trade_2_ask', 'trade_2_bid', 'trade_2_pair', 'outcome_2',
      'trade_3_ask', 'trade_3_bid', 'trade_3_pair', 'outcome_3',
      'trade_4_ask', 'trade_4_bid', 'trade_4_pair', 'outcome_4'
    ]

    valuesString = ""
    columnsString = ""
    values = [
      timestamp, exchange, arb_obj.arb_rate
    ]
    
    for trade in arb_obj.sequential_trades:
      coins.append(trade.from_coin)
      asks.append(trade.ask)
      bids.append(trade.bid)
      pairs.append(trade.symbol)

    values = values + coins

    for i in range(4): 
      values.append(asks[i])
      values.append(bids[i])
      values.append(pairs[i])
      values.append(outcomes[i])
    for i in range(len(values)):
      if isinstance(values[i], str):
        values[i] = f"'{values[i]}'"

      if (i == (len(values) - 1)):
        valuesString = valuesString + f"{values[i]}"
        columnsString = columnsString + f"{columns[i]}"
      else:
        valuesString = valuesString + f"{values[i]},"
        columnsString = columnsString + f"{columns[i]},"

    return f"INSERT INTO arb_rates ({columnsString}) VALUES ({valuesString})"