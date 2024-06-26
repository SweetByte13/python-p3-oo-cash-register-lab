#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.prices= []
    self.items = []
    
  def add_item(self,title,price,quantity=1):
    self.total += (quantity * price)
    self.prices.append(quantity * price)
    for x in range(0,quantity):
      self.items.append(title)

  def apply_discount(self, price=1000):
    if self.discount == 0:
       print("There is no discount to apply.")
    
    else:
      # discount_to_apply = self.total * (self.discount / 100)
      # self.total -= int(discount_to_apply)
      # print(f"After the discount, the total comes to ${self.total}.")
      self.total = price * (1 - self.discount / 100)
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
      
      # can flip this if/ else statment and have it: if discount, else: print
  def void_last_transaction(self):
    self.total = self.total - self.prices[-1]
    del self.prices[-1]
    del self.items[-1]

