class Calculate:

  @staticmethod
  def relative_difference(source_amount, destination_amount):
    # print(source_amount, destination_amount)
    relative_difference = round(((destination_amount - source_amount) / max(source_amount, destination_amount) * 100), 2)
    return relative_difference

  @staticmethod
  def outcome(from_amount, trade_price, trade):
    if trade.to_coin == trade.quote:
      return from_amount * trade_price
    else:
      return from_amount / trade_price