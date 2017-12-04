def n_choose_k(n, k):
    # top
    top = [i for i in range(k+1, n+1) if not i in range(1, n-k+1)]
    # bottom
    bottom = [i for i in range(1, n-k+1) if not i in range(k+1, n+1)]

    N = 1
    for t in top:
        N *= t
    D = 1
    for b in bottom:
        D *= b

    return N/D

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def answer(x, y, n):

    # x - number of rabbits seen from the first side
    # y - number of rabbits seen from the second side
    # n - total number of rabbits

    # Note: The actual hieghts of the rabbits are immaterial to the solution
    # The ranking of the rabbits (1, 2, 3, ... n) is all the matters

    # Note n is never supposed to be < 3, but this method is generalized to work for all n > 0

    def oneway_solve(x, n):
        # Check if solution table already exists, if not, create it
        if not hasattr(oneway_solve, "table"):
            oneway_solve.table = {}
        # Check the solution table for a previous answer
        if oneway_solve.table.get((x, n)):
            return oneway_solve.table.get((x, n))
        # Note: Special cases where n < 3 
        if n <= 2:
            return 1

        # If the tallest rabbit is in front, the number of combinations of the rabbits
        # standing behind the tallest rabbit is just the factorial of n-1
        if x <= 1:
            return factorial(n-1)
        else:
            # Identify the possible positions of the tallest rabbit
            max_positions = [i for i in range(x-1,n)]

        p = 0
        for mp in max_positions:
            # This problem can be solved recursively by removing all of the rabbits behind
            # the current tallest rabbit. However, there are two factor to consider.
            # Each rabbit could be to the left or right of the tallest rabbit, which creates
            # a n choose k number of combinations (right/left choose factor).
            # Also, the rabbits past the tallest rabbit can be in any order since no information
            # is known about their size/order. This creates a factorial number of combinations for
            # that group.
            # Multiply all of the factors together to get the solution for this possible position
            # for the tallest rabbit, and recurse down until there are fewer than 3 rabbits remaining.
            rl_choose_factor = n_choose_k(n-1, mp)
            right_ambiguity = factorial(n-mp-1)
            p += oneway_solve(x-1, mp) * rl_choose_factor * right_ambiguity

        # Add the current answer to the solution table for future use
        oneway_solve.table[(x, n)] = p
        
        return p
           
    # Note: if both x and y are 1, then the configurations is impossible for n > 1
    if x == 1 and y ==1:
        if n == 1:
            # Trivial Case
            return "1"
        else:
            # Impossible Case
            return "0"

    # Identify the possible positions of the tallest rabbit
    if x == 1:
        max_positions = [0]
    elif y == 1:
        max_positions = [n-1]
    else:
        max_positions = [i for i in range(x-1, n-y+1)]

    # Find the number of possible combinations for each possible position of the tallest rabbit
    combinations = 0
    for mp in max_positions:
        # The position of the tallest rabbit can be used to devide the problem into two chuncks
        # Any positions to the left/right of the tallest rabbit don't count to the number the guard on
        # the other side can see.
        # The one_way_solve function takes two parameters, number of rabbits seen (x) and total rabbits (n)
        # and provides the number of combinations that can meet that requirement
        right = oneway_solve(x-1, mp)
        left = oneway_solve(y-1, n-mp-1)
        # Since the tallest rabbit splits the problem into two independent problems, the resulting combinations
        # are the product of the two answers, multiplied by the n choose k factor which represents all the different
        # ways the rabbits can be split between the two sides.
        combinations += (right * left) * n_choose_k(n-1,mp)

    return "%s" % combinations

            
#print n_choose_k(10,2)
#print n_choose_k(3, 2)
#print n_choose_k(40,20)

#print factorial(38)

print answer(1,1,5) == "0"
print answer(2,1,5) == "6"
print answer(3,1,5) == "11"
print answer(4,1,5) == "6"
print answer(5,1,5) == "1"
print answer(3,2,5) == "18"
print answer(2,2,3) == "2"
print answer(1,2,6) == "24"
print answer(1,2,40) == "523022617466601111760007224100074291200000000"
print answer(4,5,40) == "41339658777121324439468104957393529276094873600"
