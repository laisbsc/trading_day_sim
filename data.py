import random
import uuid
from decimal import Decimal


# number of companies and investors instantiated
NUMBER_OF_INSTANCES = 10


class Investor:

    # def __init__(self, id_inv, budget, acq_shares=0):
    #     """ Constructor for the Investor object """
    #     self.id_inv = id_inv
    #     self.budget = budget
    #     self.acq_shares = acq_shares

    def __repr__(self):
        """ toString() method for the Investors class """
        return f"<Budget:{self.budget} Acquired shares:{self.acq_shares}>\n"

    def set_budget(self, funds):
        _budget = funds

    def get_budget(self):
        return self.budget

    def has_money(self):
        """checks if the investor has money to trade"""
        if self.budget > 0:
            return True

    def trade(self, company):
        """ Swaps investor's money for companies's shares"""
        new_budget = self.budget - company.share_price
        company.shares_num -= 1
        self.acq_shares += 1
        self.budget = new_budget
        return self


    # def sell_shares(self, company):
    #     """ sells the shares from companies to investors - changed my mind """
    #     trade = self.budget - company.get_share_price
    #     Company.get_shares_num -= 1
    #     self.acq_shares += 1
    #     self.budget = trade
    #     return self



class Company:

    def __init__(self, id, shares_num, share_price):
        """ Constructor for the Company object """
        self.id = id
        self.shares_num = shares_num
        self.share_price = share_price
        self.is_trading()

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

    def is_trading(self):
        if self.shares_num > 0:
            return True

    # def comp_select(self):
    #     for comp in companies:
    #         comp_choice = comp[]
    #         return comp_choice


# instantiating companies (using list comprehension)
comp = [Company(id=str(uuid.uuid4().hex), shares_num=random.randint(500, 1000), share_price=Decimal(random.randint(10, 100))) for _ in range(NUMBER_OF_INSTANCES)]
companies = {c.id: c for c in comp}
print("List of companies: \n", companies)

# instantiating investors (using list comprehension)
inv = [Investor(id_inv=str(uuid.uuid1().hex), budget=random.randint(50_000, 100_000)) for _ in range(NUMBER_OF_INSTANCES)]
investors = {i.id_inv: i for i in inv}
print("List of Investors: \n", investors)

for inv in investors:
    print(inv[0])


# # sample for testing pre-trade
# print("pre trading: ", inv[0], comp[0])
# print("pre trading: ", inv[1], comp[1])
# print("pre trading: ", inv[2], comp[2])


def trade_all(invs, comps):
    """ function that keeps looping through """
    for inv in investors:
        for comp in companies:
            # while Investor.has_money is True and Company.is_trading is True:
            for (i, c) in zip(inv, comp):
                Investor.trade(i, c)
                print("Trade successful")
            # else:
            #     break

    # for inv in investors:
    #     for comp in companies:
    #         while Investor.has_money is True and Company.is_trading is True:
    #             Investor.trade(inv, comp)
    #             print("investors now have: ", inv)
    #         else:
    #             print("there are no more available shares or investor's money to trade")
    #             break

trade_all(investors, companies)

    # trade(inv, comp)

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

