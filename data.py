import random
import string


class Company(object):
    """
    initializes the Company object
    """

    def __init__(self, id, is_trading=True):
        self.id = id
        self.is_trading = is_trading

    # I'm aware this is best practice but I couldn't make it work
    # def __init__(self, id, share_number, share_price, is_trading=True):
    #     self.id = id
    #     self.share_number = share_number
    #     self.share_price = share_price
    #     self.is_trading = is_trading

    @property
    def ran_id_gen(self):
        return ''.join([random.choice(string.ascii_uppercase
                                      + string.digits) for n in range(6)])

    @ran_id_gen.setter
    def ran_id_gen(self, id):
        self.id = id

    @property
    def share_number(self):
        return random.randint(500, 1000)

    @share_number.setter
    def share_number(self, shares):
        self.share_number = shares

    @property
    def share_price(self):
        return random.randint(10, 100)

    @share_price.setter
    def share_price(self, price):
        self.share_price = price


class Investor(object):
    """
    initializes the Investor object
    """
    def __init__(self, id, is_trading=True):
        self.id = id
        self.is_trading = is_trading

    @property
    def ran_id_gen(self):
        return ''.join([random.choice(string.ascii_uppercase
                                      + string.digits) for n in range(4)])

    @ran_id_gen.setter
    def ran_id_gen(self, id):
        self.id = id

    @property
    def budget(self):
        return random.randint(1000, 10000)

    @budget.setter
    def budget(self, budget):
        self.budget = budget


# instantiating the companies list
companies = [Company(id) for _ in range(10)]

# instantiating the investors list
investors = [Investor(id) for _ in range(2)]

print('Set of companies: ')
for company in companies:
    print('Company ID(unique): ', company.ran_id_gen, '\n\tNumber of shares: ', str(company.share_number), ' units',
          '\tPrice of shares: $', str(company.share_price), '\tStatus: ', 'available')
companies.append(company)

print('\nSet of investors: ')
for investor in investors:
    print('Investor ID(unique): ', investor.ran_id_gen, '\n\tBudget: $', str(investor.budget), '\tStatus: ', 'available')
investors.append(investor)


def trade(self):
    pass
