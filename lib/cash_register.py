#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
        self.total = 0
        self.transactions = []
        self.items = []
        self.discount = discount

  def add_item(self, item_name, price, quantity=1):
        for _ in range(quantity):
            self.transactions.append(price)
            self.items.append(item_name)
            self.total += price

  def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
            self.items.pop()

  def reset_register_totals(self):
        self.total = 0
        self.transactions = []
        self.items = []

  def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

class TestCashRegister:

    cash_register = CashRegister()
    cash_register_with_discount = CashRegister(20)

    def reset_register_totals(self):
        self.cash_register.reset_register_totals()
        self.cash_register_with_discount.reset_register_totals()

    def test_discount_attribute(self):
        assert self.cash_register.discount == 0
        assert self.cash_register_with_discount.discount == 20 