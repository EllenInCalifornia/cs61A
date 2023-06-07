import sys

from pair import *
from scheme import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        '''scheme_eval(Pair('+', Pair(2, Pair(2, nil))), create_global_frame())
         expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))') 
        '''
        # in map function, mapped = fn(self.first), but scheme_eval has two arguments
        operator = scheme_eval(expr.first, env)
        # if isinstance(operator, LambdaProcedure):
        #     return scheme_apply(operator, expr.rest, env)
        operands = expr.rest.map(lambda x: scheme_eval(x, env))
        return scheme_apply(operator, operands, env)



def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):

        func = procedure.py_func
        argu = []
        while args != nil:
            argu.append(args.first)
            args = args.rest

        try:
            if procedure.need_env:
                return func(*argu, env)
            else:
                return func(*argu)
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        formals = procedure.formals
        # vals = args.map(lambda x: scheme_eval(x, env))
        current_frame = env.make_child_frame(formals, args)
        return eval_all(procedure.body, current_frame)

        # body:  Pair(Pair("+", Pair("x", Pair(2, nil))), nil)

        # END PROBLEM 9

    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
# (define outer-func (lambda (x y) (define inner (lambda (z x) (+ x (* y 2) (* z 3)))) inner))


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    result = None
    expr = expressions
    while expr != nil:
        result = scheme_eval(expr.first, env)
        expr = expr.rest
    return result


      # replace this with lines of your own code
    # END PROBLEM 6


class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val
