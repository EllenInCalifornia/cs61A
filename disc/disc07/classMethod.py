"""
A method can be turned into a class method by adding the classmethod decorator.
 Then, instead of receiving the instance as the first argument (self),
 the method will receive the class itself (cls).
 Class methods are commonly used to create "factory methods":
 methods whose job is to construct and return a new instance of the class.
"""
class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    @classmethod
    def robo_factory(cls, owner):
        return cls("RoboDog", owner)
    '''we don't have to explicitly pass in the Dog class as the cls argument, 
    since Python implicitly does that for us. '''

    # With other previously defined methods not written out