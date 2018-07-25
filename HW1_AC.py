# Ambreen Chaudhri
# Python Homework 1

import random
import time

class Portfolio(object): 
# This first function uses "class instantiation" to create a generic instance of 
# the class that will be populated later when creating a particular instance.
  
  def __init__(self, cash=0, stocks=0, stock_buyprices=0, funds=0, fund_buyprices=0, transactions=0):
    				# 'Self' must be the generic first argument used.
    				# If we designate cash = 0, we do not have to
    				# provide a value for this variable.	
    self.cash = cash # The object or instance variable 'cash' is an 
        			 # attribute for the class Portfolio. 
    self.stocks = {}
    self.stock_buyprices={}
    self.funds = {}
    self.fund_buyprices ={}
    now = time.strftime("%c") # taken from http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
    self.transactions = []
    self.transactions.append("The account was created on %s." % now)  

  def __str__(self):
    return "\nTotal Cash: $%.2f \nStocks: %s \nMutual Funds: %s" %(self.cash, self.stocks, self.funds)
       
  def addCash(self, amount):
	if amount > 0:
	  self.cash += amount
	  now = time.strftime("%c")
	  self.transactions.append("On %s, $%.2f was added to cash holdings." %(now, amount))
	  return "$%.2f" %self.cash
	else:
	  return "Please enter an appropriate cash amount to withdraw." 
    
  
  def withdrawCash(self, amount):
    if amount > 0 and amount <= self.cash:
      self.cash -= amount
      now = time.strftime("%c")
      self.transactions.append("On %s, $%.2f was withdrawn from cash holdings." %(now, amount))
      return "$%.2f" %self.cash
    else:
	  	return "You have insufficient funds to withdraw." 

  def buyStock(self, shares, stock):
    if shares > 0 and isinstance(shares, int) == True and isinstance(stock, Stock) == True:
# This tests whether the number of shares is an integer from http://stackoverflow.com/questions       
      if shares*stock.buyprice <= self.cash:
        if (not (stock.ticker_code in self.stocks.keys())):
        	shares= int(shares)
        	self.stocks[stock.ticker_code]=0
        	self.stock_buyprices[stock.ticker_code]=stock.buyprice
        self.stocks[stock.ticker_code] += shares 
        self.cash -= shares*stock.buyprice
        now = time.strftime("%c")
        self.transactions.append("On " + str(now) + ", " + str(shares) + " shares of " + stock.ticker_code + " stock at $" + str(stock.buyprice) + " were purchased.")
        return "You purchased %s shares of %s stock." %(shares, stock.ticker_code)
      else:
       return "You have insufficient funds to complete the transation."
    else:
      return "Only whole shares of stocks that are available can be purchased.  Please enter an integer value or designate the ticker and sell price first."

  def buyMutualFund(self, shares, stock):
    if shares > 0 and type(shares)!=int and isinstance(stock, MutualFund) == True:
      if shares*1 <= self.cash:
        if (not (stock.ticker_code in self.funds.keys())):
        	self.funds[stock.ticker_code]=0
        	self.fund_buyprices[stock.ticker_code]=stock.buyprice
        self.funds[stock.ticker_code] += shares 
        self.cash -= shares*stock.buyprice
        now = time.strftime("%c")
        self.transactions.append("On " + str(now) + ", " + str(shares) + " shares of " + stock.ticker_code + " mutual fund at $1 per share were purchased.")
        return "You purchased %s shares of %s mutual fund." %(shares, stock.ticker_code)
      else:
       return "You have insufficient funds to complete the transation."
    else:
      return "Only fractional shares of mutual funds that are available can be purchased.  Please enter an integer value or designate the mutual fund code first."

  def sellStock(self, ticker, shares):
    if shares > 0 and ticker in self.stocks.keys():
			if self.stocks[ticker] >= shares:
				self.stocks[ticker] -= shares
				s=Stock(self.stock_buyprices[ticker], ticker)
				self.cash += shares*s.sellprice()
				now = time.strftime("%c")
				self.transactions.append("On " + str(now) + ", " + str(shares) + " shares of " + ticker + " stock were sold at $" + str(round(s.sellprice(),2)) + ".")
				return "You sold %s shares of %s stock." %(shares, ticker)
			else:
				return "Please select fewer shares."
    else:
      return "You cannot sell a stock you do not own."
      
      
  def sellMutualFund(self, code, shares):
    if shares > 0 and code in self.funds.keys():
			if self.funds[code] >= shares:
				self.funds[code] -= shares
				s=MutualFund("foo",self.fund_buyprices[code])
				self.cash += shares*s.sellprice()
				now = time.strftime("%c")
				self.transactions.append("On " + str(now) + ", " + str(shares) + " shares of " + code + " mutual fund were sold at $" + str(round(s.sellprice(),2)) + ".")
				return "You sold %s shares of %s mutual fund." %(shares, code)
			else:
				return "Please select fewer shares."
    else:
      return "You cannot sell a stock you do not own."
             
    
  def history(self):
    return ("\n".join(self.transactions))



# Create a Class called Asset (which is the parent class).  It uses Inheritance with
# the sub-classes for specific asset types: stocks and mutual funds.

class Asset(object):

  def __init__(self, buyprice, ticker_code):
    self.ticker_code = ticker_code
    self.buyprice = buyprice
      
class Stock(Asset):
     
  def __init__(self, buyprice, ticker_code):
    Asset.__init__(self, buyprice, ticker_code)   
     
  def sellprice(self):
		return round(random.uniform(.5, 1.5)*self.buyprice , 2)
    
  def __str__(self):
  	return "Ticker: %s and BuyPrice: $%s" % (self.ticker_code, self.buyprice)
  
class MutualFund(Asset):
  
  def __init__(self, ticker_code, buyprice=0):
    Asset.__init__(self, 1, ticker_code)
  
  def sellprice(self):
    return round(random.uniform(0.9, 1.2),2)
  
  def __str__(self):
  	return "Code: %s" % (self.ticker_code)


class Bonds(Asset):

  def __init__(self, buyprice, ticker_code):
    Asset.__init__(self, buyprice, ticker_code)

  def __str__(self):
  	return "Bond: %s and BuyPrice: %s" % (self.ticker_code, self.buyprice)


#Test 1: Creates a new portfolio
portfolio = Portfolio()
print(portfolio)

portfolio2 = Portfolio(cash=100)
print(portfolio2)

# Test 2: Adds cash to the portfolio
print portfolio.addCash(300.50) 

# Test 3: Create stock with a buyprice of 20 and ticker "HFH"
s = Stock(20, "HFH")
print s.__str__()
print s.sellprice()

# Test 4: Buy 5 shares of stock s
print portfolio.buyStock(5,s)

# Test 5: Create a Mutual Fund with the code "BRT"
mf1 = MutualFund("BRT")
print mf1.__str__()
print mf1.sellprice()

# Test 6: Create a Mutual Fund with the code "GHT"
mf2 = MutualFund("GHT")
print mf2.__str__()
print mf2.sellprice()

# Test 7: Buy 10.3 shares of "BRT"
print portfolio.buyMutualFund(10.3,mf1)

# Test 8: Buy 2 shares of "GHT"
print portfolio.buyMutualFund(2,mf2)

# Test 9: Print portfolio
print(portfolio) 

# Test 10: Sell 3 shares of "BRT mutual fund"
print portfolio.sellMutualFund("BRT", 3)

# Test 11: Sell 1 share of "HFH" stock
print portfolio.sellStock("HFH", 1)

# Test 12: Remove $50
print portfolio.withdrawCash(50)

# Test 13: Print history of transactions
print portfolio.history()


