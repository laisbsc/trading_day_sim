import random
import uuid
from decimal import Decimal

# kinda working but trade_all() is messed up

# number of companies and investors instantiated
NUMBER_OF_INSTANCES = 100


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

    def has_money(self):
        """checks if the investor has money to trade"""
        if self.budget > 0:
            return True

    def trade(self, company):
        """ Swaps investor's money for companies's shares - in class"""
        new_budget = self.budget - company.share_price
        company.shares_num -= 1
        self.acq_shares += 1
        self.budget = new_budget


# def trade(Investor, Company):
#     """ Swaps investor's money for companies's shares - outter class [testing purposes]"""
#     new_budget = Investor.budget - Company.share_price
#     Company.shares_num -= 1
#     Investor.acq_shares += 1
#     Investor.budget = new_budget


class Company:

    def __init__(self):
        """ Constructor for the Company object """
        self.id: str = uuid.uuid4().hex
        self.shares_num = random.randint(500, 1000)
        self.share_price = Decimal(random.randint(10, 100))
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


# instantiating companies (using list comprehension)
comp = [Company() for _ in range(NUMBER_OF_INSTANCES)]
companies = {c.id: c for c in comp}
print("List of companies: \n", companies)

# instantiating investors (using list comprehension)
inv = [Investor() for _ in range(NUMBER_OF_INSTANCES)]
investors = {i.id_inv: i for i in inv}
print("List of Investors: \n", investors)


# def trade_all(invs, comps):
#     """ function that keeps looping through >> returning an infinite loop"""
#     for inv in investors:
#         for comp in companies:
#             # while Investor.has_money is True and Company.is_trading is True:
#             for (i, c) in zip(inv, comp):
#                 Investor.trade(i, c)
#                 print("Trade successful")
#             # else:
#             #     break


def trade_all(invs, comps):
    """ function that trades between investors and shares - kinda works, just not dynamic"""
    while Investor.has_money is True and Company.is_trading is True:
        for index in range(len(investors)):
            for index_ in range(len(companies)):
                # for (i, c) in zip(inv, comp):
                Investor.trade(inv[index], comp[index_])
                print("Companies: " + str(comp[index]), "Investors: " + str(inv[index]))
    else:
        print("Sorry, no more assets available to trade. Check your resources.")

# calling trade_all function
trade_all(investors, companies)

""" 'test' for trade function with individual instances"""
# making instances trade individually
# trade(inv[0], comp[0])
# trade(inv[0], comp[1])
# trade(inv[0], comp[2])
# trade(inv[1], comp[0])
# trade(inv[1], comp[1])

# printing post-trade result
print("POST TRADING: ")
print(f" Investor I: {inv[0]} Company I: {comp[0]}")
print(f" Investor II: {inv[1]} Company II: {comp[1]}")
print(f" Investor III: {inv[2]} Company III: {comp[2]}")
