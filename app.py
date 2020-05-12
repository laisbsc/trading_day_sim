import random
import string
import uuid
from decimal import Decimal


class Investor():

    def __init__(self):
        self.str: int = uuid.uuid4().hex
        self.budget: Decimal = random.randint(50_000, 100_000)


class Company():

    def __init__(self, is_trading=True):
        """
        initializes the Company object
        """
        self.id: str = uuid.uuid4().hex
        self.is_trading = is_trading
        self.shares_num = random.randint(500, 1000)
        self.share_price = Decimal(random.randint(10, 100))

    def collapse(self):
        self.share_price *= 0.98

    def soar(self):
        self.share_price *= 2

    def __str__(self):
        return f"<Cpy shares:{self.shares_num} price:{self.share_price}>"

    def __repr__(self):
        return f"<Cpy shares:{self.shares_num} price:{self.share_price}>"


aa = [Company() for _ in range(10)]

market = {c.id: c for c in aa}
print(market)
