# Trading-day simulator
Design and Implementation of a simplified model trading simulator using Design Patterns.
The program dynamically generates 100 companies (with random unique IDs, shares amount and prices, and availability to trade) and 100 investors (with random unique ID, a budget to buy shares and a trading status).
# The scenario
A typical trading day is characterized by investors buying ONE share from each company at each time. When a company sells 10 shares, any company that haven't sold any of their shares will have their share price decreased by 2%. Any time a company sells 10 shares, their share price will increase by 100% (double). To keep track of those changes, I used the Moderator Design Patter.
The trading ends once investors have no more money OR there are no more available shares to buy.
When finalised, the program will prompt the user with a menu showing options to return different types of report.
___________________________________________________________________________________

# Design Patterns
# Justification
Design patterns are a common way of solving well known problems. Two main principles are in the bases of the design patterns defined by the GOF:

    Program to an interface not an implementation.
    Favor object composition over inheritance.

The Observer defines a one-to-many relationship so that when one object changes state, the others are notified and updated automatically. In this case, it was used so that everytime a trade happened, the share_number state would change. And for each 10 shares sold on the market, the companies with curr_share_numer equals to their init_share_number had their share_price *= 0.98.

Moderator instead of observer - https://sourcemaking.com/design_patterns/mediator introduce "an additional level of indirection" - take the mapping of users to groups and groups to users, and make it an abstraction unto itself. This offers several advantages: Users and Groups are decoupled from one another, many mappings can easily be maintained and manipulated simultaneously, and the mapping abstraction can be extended in the future by defining derived classes. The Mediator defines an object that controls how a set of objects interact. Loose coupling between colleague objects is achieved by having colleagues communicate with the Mediator, rather than with each other. The control tower at a controlled airport demonstrates this pattern very well. The pilots of the planes approaching or departing the terminal area communicate with the tower rather than explicitly communicating with one another. The constraints on who can take off or land are enforced by the tower. It is important to note that the tower does not control the whole flight. It exists only to enforce constraints in the terminal area. Mediator leverages Observer for dynamically registering colleagues and communicating with them.
