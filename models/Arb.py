from models.Calculate import Calculate
from models.CcxtRest import CcxtRest

class Arb:
  def __init__(self, sequential_trades):
    self.sequential_trades = sequential_trades
    self.outcomes = []
    self.arb_rate = self.from_sequence()

  def from_sequence(self, start_amount = 1000):
    first_trade = self.sequential_trades[0]

    if (first_trade.side == 'buy'):
      first_price = self.sequential_trades[0].ask
    else:
      first_price = self.sequential_trades[0].bid

    first_outcome = Calculate.outcome(start_amount, first_price, first_trade)
    self.outcomes.append(first_outcome)

    for i, trade in enumerate(self.sequential_trades):
      if i > 0:
        previous_end_amount = self.outcomes[i - 1]

        if trade.side == 'buy':
          price = trade.ask
        elif trade.side == 'sell':
          price = trade.bid

        outcome = Calculate.outcome(previous_end_amount, price, trade)
        self.outcomes.append(outcome)

    arb_rate = Calculate.relative_difference(start_amount, self.outcomes[-1])
    return arb_rate