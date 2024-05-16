#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.prices= []
    self.items = []
    
  def add_item(self,title,price,quantity=1):
    self.total += (quantity * price)
    for x in range(0,quantity):
      self.items.append(title)
      self.prices.append(quantity * price)
    
  def apply_discount(self, price=1000):
    if self.discount == 0:
       print("There is no discount to apply.")
    
    else:
      self.total = price * (1 - self.discount / 100)
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
   
  
  def void_last_transaction(self):
    self.total = self.total - self.prices[-1]
    del self.prices[-1]
    if self.items == None:
      return self.total