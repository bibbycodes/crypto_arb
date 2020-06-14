class Parse:
	@staticmethod
	def trade(trade, from_coin, to_coin):
		if from_coin == trade['base']:
			side = "sell"
		else:
			side = "buy"

		return {
			"symbol" : trade['symbol'],
      "trade_pair" : trade['id'],
      "from_coin" : from_coin,
      "to_coin"   : to_coin,
      "side" : side,
      "quote" :  trade['quoteId'],
      "base" : trade['baseId'],
      "precision" : trade['precision'],
      "taker_fee" : trade['taker'],
      "maker_fee" : trade['maker'],
      "limits" : trade['limits']
		}