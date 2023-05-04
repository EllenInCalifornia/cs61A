class TeamMember:
    def __init__(self, operation, prev_member=None):
        """
        A TeamMember object is instantiated by taking in an `operation`
        and a TeamMember object `prev_member`, which is the team member
        who "sits in front of" this current team member. A TeamMember also
        tracks a `history` list, which contains the answers given by
        each individual team member.
        """
        self.history = []
        self.operation = operation
        self.prev_member = prev_member

    def relay_calculate(self, x):
        """
        The relay_calculate method takes in a number `x` and performs a
        relay by passing in `x` to the first team member's `operation`.
        Then, that answer is passed to the next member's operation, etc. until
        we get to the current TeamMember, in which case we return the
        final answer, `result`.
        """
        if self.prev_member == None:
            res = self.operation(x)
            self.history = [res]
        else:
            # use recursion
            pre = self.prev_member
            pre_res = pre.relay_calculate(x)
            res = self.operation(pre_res)
            self.history = pre.history + [res]
        return res



    def relay_history(self):
        """
        Returns a list of the answers given by each team member in the
        most recent relay the current TeamMember has participated in.
        """
        return self.history