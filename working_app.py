import uuid
from decimal import Decimal
from typing import List
import random

""" NOTE FOR TEACHER:
This file should not be consider for grading purposes since it is not
the student's code.

This code was written by Nicolas Laurence on 18/05/2020.
As a bet that the app could be written in under an hour ¬¬' and
without the use of design patterns [my friends are dicks, I know!]"""


class Investor():

    def __init__(self, market):
        """
        initializes the Investor object
        """
        self.id = uuid.uuid4().hex[:6]
        self.budget: Decimal = random.randint(1_000, 10_000)
        self.portfolio = {}
        self.market = market

    def buy(self, company):
        return self.market.transaction(self, company)

    @property
    def worth(self):
        shares = sum([self.market.companies[cpy].share_price * volume for cpy, volume in self.portfolio.items()])
        return shares

    def __repr__(self):
        return f"<Inv id:{self.id} budget:{self.budget} worth:{self.worth}>"

class Company():

    def __init__(self):
        """
        initializes the Company object
        """
        self.id: str = uuid.uuid4().hex[:6]
        self.shares_num = random.randint(500, 1000)
        self.share_price = Decimal(random.randint(10, 100))
        self.cash = 0
        self.sold_shares = 0
        self.owners = {}

    def rally(self):
        """if a company sells 10 shares price doubles"""
        if self.sold_shares > 0 and not self.sold_shares % 10:
            self.share_price *= 2

    def __repr__(self):
        return f"<Cpy shares:{self.shares_num} price:{self.share_price}>"


class Market():
    def __init__(self, companies: List[Company]):
        self.companies = {c.id: c for c in companies}
        self.transaction_count = 0

    def transaction(self, buyer, seller):
        if not buyer.budget >= seller.share_price:
            return False
        if seller.sold_shares >= seller.shares_num:
            return False
        buyer.budget -= seller.share_price
        buyer.portfolio[seller.id] = buyer.portfolio.get(seller.id, 0) + 1

        seller.cash += seller.share_price
        seller.owners[buyer.id] = seller.owners.get(buyer.id, 0) + 1
        seller.sold_shares += 1
        seller.rally()

        self.transaction_count += 1
        self.update()

    def update(self):
        """every 10 transaction price drops for company who haven't sold any share"""
        if not self.transaction_count % 10:
            for cpy in [c for c in self.companies.values() if not c.sold_shares]:
                cpy.share_price *= .98

    def smallest_share_price(self):
        return min([cpy.share_price for cpy in self.companies.values()])

    def trading_companies(self):
        return [c for c in self.companies.values() if c.sold_shares < c.shares_num]


market = Market([Company() for _ in range(10)])
investors = [Investor(market) for _ in range(10)]

players = [i for i in investors if i.budget > market.smallest_share_price()]
trading = market.trading_companies()

while players and trading:
    for investor in players:
        random.shuffle(trading)
        for company in trading:
            investor.buy(company)
        trading = market.trading_companies()
    players = [i for i in investors if i.budget > market.smallest_share_price()]

import operator
richest = sorted(investors, key=operator.attrgetter('worth'), reverse=True)
print(richest[0])
