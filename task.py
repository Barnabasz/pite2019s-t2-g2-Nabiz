#!/usr/bin/python3

class Bank():
	def __init__(self,name):
		self.name = name
		self.accounts = {}
	def addAccount(self,client):
		acc = Account(client)
		self.accounts[acc.number] = acc
	def event(self,accNum, evName, money=0):
		if evName == "deposit":
			self.accounts[accNum].deposit(money)
		elif evName == "withdraw":
			self.accounts[accNum].withdraw(money)
		elif evName == "balance":
			return self.accounts[accNum].getBalance()

class Client():
	def __init__(self,name):
		self.name = name
	
class Account():
	number = 0
	def __init__(self, client):
		Account.number +=1
		self.number = Account.number
		self.balance = 0
		self.client = client
	def getBalance(self):
		return self.balance

	def deposit(self,money):
		self.balance+=money

	def withdraw(self,money):
		self.balance-=money

		
client1 = Client("David")
print(client1.name)

bank1 = Bank("PKO")
bank1.addAccount(client1)

bank1.event(1,"deposit",100)
print(bank1.event(1,"balance"))
bank1.event(1,"withdraw",50)
print(bank1.event(1,"balance"))