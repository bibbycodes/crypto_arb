class Calculate:
  @staticmethod
  def relative_difference(priceA, priceB):
    relative_difference = round(((priceA - priceB) / max(priceA, priceB) * 100), 2)
    return relative_difference

  @staticmethod
  def outcome(from_amount, trade_price, trade):
    if trade['to'] == trade['quote']:
      return from_amount * trade_price
    else:
      return from_amount / trade_price