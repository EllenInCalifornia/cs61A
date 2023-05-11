def mod_7(n):
    if n % 7 == 0:
        return 0
    else:
        return 1 + mod_7(n - 1)
""" Constant, since in the worst case scenario our
 function mod_7 will require 6 recursive calls to 
 reach the base case.Since the growth of the computation is independent of the input, 
 we say this is constant, which is commonly known as a Θ(1) runtime. """