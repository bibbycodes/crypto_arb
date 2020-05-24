class Validate:
  @staticmethod
  def pair_exists(markets, pair):
    if pair in markets.keys():
      return True
    return False

  @static_method
  def correct_pair(markets, quote, base):
    forward = '{}/{}'.format(quote.upper(), base.upper())
    backward = '{}/{}'.format(base.upper(), quote.upper())
    market_keys = markets.keys()

    if forward in market_keys:
      return forward
    elif backward in market_keys:
      return backward
    else:
      return False

  @staticmethod
  def side(from_coin, base):
    if from_coin == base:
      return 'sell'
    return 'buy'

  @staticmethod
  def switch_pairs(pair):
    split_pair = pair.split('/')
    return '{}/{}'.format(split_pair[1], split_pair[0])