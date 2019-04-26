#!/usr/bin/env python3

import unittest
from task import Bank, Client, Account

class BankTest(unittest.TestCase):
	def test_createBank(self):
		self.bank = Bank("bank")
	def test_addAccount(self):
		self.bank = Bank("bank")
		self.client = Client("Client")
		self.bank.addAccount(self.client)
	def test_event(self):
		self.bank = Bank("bank")
		self.client = Client("client")
		self.bank.addAccount(self.client)
		self.bank.event(0,"withdraw",50)
		self.bank.event(0,"deposit",100)
		self.bank.event(0,"balance")