# VirFib 很有意思，用instance attribute 来store value

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2022
    >>> dime = mint.create(Dime)
    >>> dime.year
    2022
    >>> Mint.present_year = 2102  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2022
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2102
    >>> Mint.present_year = 2177     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2022

    def __init__(self):
        self.update()

    def create(self, coin):
        new_coin = coin(self.year)
        return new_coin

    def update(self):
        self.year = Mint.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        age = Mint.present_year - self.year
        value = self.cents
        if age > 50:
            value += (age - 50)
        return value


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        self.stock = 0
        self.product = product
        self.balance = 0
        self.price = price
    def restock(self, n):
        self.stock += n
        return 'Current ' + self.product + ' stock: ' + str(self.stock)
    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        elif self.balance < self.price:
            return 'Please add $' + str(self.price - self.balance) + ' more funds.'
        elif self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return 'Here is your candy and $' + str(change) +' change.'
        else:
            self.balance = 0
            self.stock -= 1
            return 'Here is your ' + self.product +'.'
    def add_funds(self, n):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock. Here is your $' + str(n) +'.'
        self.balance += n
        return 'Current balance: ' + '$' + str(self.balance)







def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]

    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random


random = make_test_random()

# Phase 1: The Player Class


class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135

    """

    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        p1 = self.popularity
        p2 = other.popularity
        win_prob = max(0.1, p1 / (p1 + p2))
        r = random()
        if r < win_prob:
            self.popularity += 50
        else:
            self.popularity -= 50
            if self.popularity < 0:
                self.popularity = 0

    def speech(self, other):
        p1 = self.popularity
        p2 = other.popularity
        self.votes += p1 // 10
        self.popularity += p1 // 10
        other.popularity -= p2 // 10




    def choose(self, other):
        return self.speech


# Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            if self.turn % 2 == 0:
                self.p1.choose(self.p2)(self.p2)
            else:
                self.p2.choose(self.p1)(self.p1)
            self.turn += 1
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        if self.p1.votes > self.p2.votes:
            return self.p1
        elif self.p1.votes < self.p2.votes:
            return self.p2
        return None


# Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def choose(self, other):
        if self.popularity <= other.popularity:
            return self.debate
        else: return self.speech



class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False

    """

    def choose(self, other):
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech


class VirFib():
    """A Virahanka Fibonacci number.

    >>> start = VirFib()
    >>> start
    VirFib object, value 0
    >>> start.next()
    VirFib object, value 1
    >>> start.next().next()
    VirFib object, value 1
    >>> start.next().next().next()
    VirFib object, value 2
    >>> start.next().next().next().next()
    VirFib object, value 3
    >>> start.next().next().next().next().next()
    VirFib object, value 5
    >>> start.next().next().next().next().next().next()
    VirFib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    VirFib object, value 8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            res = VirFib(1)
        else:
            res = VirFib(self.value + self.previous)
        res.previous = self.value
        return res
# storing the current value makes the
# solution look very similar to the iterative version of the virfib problem.



    def __repr__(self):
        return "VirFib object, value " + str(self.value)
