import random
import uuid
from decimal import Decimal

# number of companies and investors instantiated
number_of_instances = 10


class Investor:

    def __init__(self, acq_shares=0):
        """ Constructor for the Investor object """
        self.id_inv = uuid.uuid1().hex
        self.budget = Decimal(random.randint(50_000, 100_000))
        self.acq_shares = acq_shares

    def __repr__(self):
        """ toString() method for the Investors class """
        return f"<Budget:{self.budget} Acquired shares:{self.acq_shares}>\n"

    def set_budget(self, funds):
        _budget = funds

    def get_budget(self):
        return self.budget

    # def sell_shares(self, company):
    #     """ sells the shares from companies to investors - changed my mind """
    #     trade = self.budget - company.get_share_price
    #     Company.get_shares_num -= 1
    #     self.acq_shares += 1
    #     self.budget = trade
    #     return self


class Company:

    def __init__(self, isTrading=True):
        """ Constructor for the Company object """
        self.id: str = uuid.uuid4().hex
        self.is_trading = isTrading
        self.shares_num = random.randint(500, 1000)
        self.share_price = Decimal(random.randint(10, 100))

    def set_shares_num(self, shares):
        _shares_num = shares

    def get_shares_num(self):
        return self.shares_num

    def set_share_price(self, price):
        _share_price = price

    def get_share_price(self):
        return self.share_price

    def collapse(self):
        """ Calculates the new share price of companies who aren't selling """
        self.share_price *= 0.98

    def soar(self):
        """ Calculates the new share price of companies who sell more """
        self.share_price *= 2

    def __str__(self):
        """ Corresponds to the toString() method in Java """
        return f"<Shares:{self.shares_num} price:{self.share_price}>"

    def __repr__(self):
        return f"<Shares:{self.shares_num} price:{self.share_price}>\n"


# instantiating companies (using list comprehension)
comp = [Company() for _ in range(number_of_instances)]
companies = {c.id: c for c in comp}
print("List of companies: \n", companies)

# instantiating investors (using list comprehension)
inv = [Investor() for _ in range(number_of_instances)]
investors = {i.id_inv: i for i in inv}
print("List of Investors: \n", inv)


def trade(investor, company):
    """ Swaps investor's money for companies's shares"""
    new_budget = investor.budget - company.share_price
    company.shares_num -= 1
    investor.acq_shares += 1
    investor.budget = new_budget
    return investor, company


# # sample for testing pre-trade
# print("pre trading: ", inv[0], comp[0])
# print("pre trading: ", inv[1], comp[1])
# print("pre trading: ", inv[2], comp[2])

def trade_all(invs, comps):
    """function that keeps looping through """
    # loop through to continue trading
    for _ in range(0, number_of_instances):
        while inv[_].budget > 0 or comp[_].share_price > 0:
            for (i, c) in zip(inv, comp):
                trade(i, c)
                print("investors now have: ", inv)
        else:
            print("there are no more available shares or investor's money to trade")
            break


# I'm prettu sure I'm calling this function wrong
trade_all(companies, investors)


# # testing post-trade
print("post trading: ", inv[0], comp[0])
print("post trading: ", inv[1], comp[1])
print("post trading: ", inv[2], comp[2])


class Transaction:

    def __init__(self, funds, update_share_price, max_shares_sell=1):
        """ not sure if this class should exist or
            if the trade_all() should be in here """
        self.funds = funds
        self.update_share_price = update_share_price
        self.max_shares_sell = max_shares_sell

    def trade(self):
        def buy():
            return self.share_price

    def buy(self, budget):
        self.budget -= comp.share_price
