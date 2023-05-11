"""
Inheritance represents a hierarchical relationship between two or more classes
where one class is a more specific version of the other
2. __init__  it is not a true constructor in the sense that it does not actually
create the object. Instead, the object is created first and then
the __init__ method is called on that object. This means that the __init__ method
can be called like any other method, after the object has been created.
"""
class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
# We can use super() to refer to the superclass of self
        super().talk()
        print('This Dog says woof!')

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives


    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        m = 'meow'
        print(f'{self.name} says {m}!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        if not self.is_alive:
            print('This cat has no more lives to lose.')
        else:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False



    def revive(self):
        """Revives a cat from the dead. The cat should now have
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            # The __init__ method is not a real constructor,
            # and can be called like any other method.
            self.__init__(self.name, self.owner)

        else:
            print('This cat still has lives to lose.')
    # (The rest of the Cat class is omitted here, but assume all methods from the Cat class above are implemented)
    def __repr__(self):
        return f'{self.name}, {self.lives} lives'
    def __str__(self):
        return f'{self.name}'




class NoisyCat(Cat):# Fill me in!
    """A Cat that repeats things twice."""
        # Is this method necessary? Why or why not?


    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()
