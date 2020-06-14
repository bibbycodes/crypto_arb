from models.Calculate import Calculate

class Trade:
  def __init__(self, trade_object, tickers):
    print(trade_object['symbol'])
    self.symbol = trade_object['symbol']
    self.trade_pair = trade_object['trade_pair']
    self.from_coin = trade_object['from_coin']
    self.to_coin = trade_object['to_coin']
    self.side = trade_object['side']
    self.quote = trade_object['quote']
    self.base = trade_object['base']
    self.precision = trade_object['precision']
    self.taker_fee = trade_object['taker_fee']
    self.maker_fee = trade_object['maker_fee']
    self.limits = trade_object['limits']
    self.ask = tickers[self.symbol]['ask']
    self.bid = tickers[self.symbol]['bid']
    self.change = tickers[self.symbol]['change']
    self.base_volume = tickers[self.symbol]['baseVolume']
    self.quote_volume = tickers[self.symbol]['quoteVolume']
    self.spread = abs(Calculate.relative_difference(self.ask, self.bid))

  def get_amount(self, previous_amount):
    if (self.from_coin == self.base):
      return previous_amount * self.bid if self.side == "sell" else self.ask
    else:
      return previous_amount