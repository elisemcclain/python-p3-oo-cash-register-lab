import ipdb

class CashRegister:
  def __init__(self, discount=0, total=0.00):
    self.discount = discount
    self.total = total
    self.items = []
    self.prices = []

  def add_item(self, title, price, quantity=1):
    for _ in range(quantity):
        self.items.append(title)
        self.prices.append(price)
        self.total += price

    self.transaction = {title: price * quantity}

  def apply_discount(self):
    discount_total = self.total * self.discount / 100
    self.total -= discount_total
    if self.total > 0:
      print(f'After the discount, the total comes to ${self.total:.0f}.')
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    if len(self.items) > 0:
      last_item_added = self.items.pop()
      self.prices.append(-abs(self.transaction[last_item_added]))
      self.total -= self.transaction[last_item_added]

    if len(self.items) == 0:
      self.total = 0.0