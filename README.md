# Trading-day simulator
Design and Implementation of a simplified model trading simulator using Design Patterns.
The program dynamically generates 100 companies (with random unique IDs, shares amount and prices, and availability to trade) and 100 investors (with random unique ID, a budget to buy shares and a trading status).
# The scenario
A typical trading day is characterized by investors buying ONE share from each company at each time. When a company sells 10 shares, any company that haven't sold any of their shares will have their share price decreased by 2%. Any time a company sells 10 shares, their share price will increase by 100% (double). To keep track of those changes, I used the Moderator Design Patter.
The trading ends once investors have no more money OR there are no more available shares to buy.
When finalised, the program will prompt the user with a menu showing options to return different types of report.
___________________________________________________________________________________

# Design Patterns
Design patterns are a common way of solving well known problems. Two main principles are in the bases of the design patterns defined by the Gang of Four:

    Program to an interface not an implementation.
    Favor object composition over inheritance.

The Observer defines a one-to-many relationship so that when one object changes state, the others are notified and updated automatically. In this case, it was used so that everytime a trade happened, the share_number state would change. And for each 10 shares sold on the market, the companies with curr_share_numer equals to their init_share_number had their price soar() with `share_price *= 0.98`.

I tried implementing the Factory pattern to create the classes (without much success).

### NOTE: the file data.py implements the Decorator, aiming to assign extra behaviors to objects at runtime without breaking the code that uses these objects. This would be used instead of the Observer. Success was equal to the Factory pattern implementation.

Source code can be found at: https://github.com/laisbsc/trading_day_sim
