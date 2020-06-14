class Validate:
  @staticmethod
  def pair_exists(markets, pair):
    if pair in markets.keys():
      return True
    return False

  @staticmethod
  def correct_pair(markets, quote, base):
    forward = f'{quote.upper()}/{base.upper()}'
    backward = f'{base.upper()}/{quote.upper()}'
    market_keys = markets.keys()

    if forward in market_keys:
      return markets[forward]
    elif backward in market_keys:
      return markets[backward]
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