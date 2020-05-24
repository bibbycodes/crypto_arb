class Calculate:
  @staticmethod
  def relative_difference(priceA, priceB):
    relative_difference = round(((priceA - priceB) / max(priceA, priceB) * 100), 2)
    return relative_difference