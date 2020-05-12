import random
import string


class Company(object):
    """
    initializes the Company object
    """

    # def __init__(self, id=0, is_trading=True):
    #     self._define_id = id
    #     self.is_trading = is_trading

    def __init__(self, id, share_number, share_price, is_trading=True):
        self.id = id
        self.share_number = share_number
        self.share_price = share_price
        self.is_trading = is_trading

    # def get_id(self):
    #     return self.id
    #
    # def set_id(self, value):
    #     value = ''.join([random.choice(string.ascii_uppercase
    #                                   + string.digits) for n in range(6)])
    #     self.id = value

    # getter for random ID generator
    @property
    def define_id(self):
        return self._define_id

    # setter for random ID generator
    @define_id.setter
    def define_id(self, id_set):
        id_set = ''.join([random.choice(string.ascii_uppercase
                                        + string.digits) for n in range(6)])
        self._define_id = id_set

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


# instantiating the companies list
companies = tuple([Company(id) for _ in range(10)])

print('Set of companies: ')
for company in companies:
    print('Company ID(unique): ', company.define_id, '\n\tNumber of shares: ', str(company.share_number), ' units',
          '\tPrice of shares: $', str(company.share_price), '\tStatus: ', 'available')
companies.append(company)

print(type(companies))


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


# instantiating the investors list
investors = [Investor(id) for _ in range(2)]


# print('\nSet of investors: ')
# for investor in investors:
#     print('Investor ID(unique): ', investor.ran_id_gen, '\n\tBudget: $', str(investor.budget), '\tStatus: ', 'available')
# investors.append(investor)


def trade(self):
    pass
