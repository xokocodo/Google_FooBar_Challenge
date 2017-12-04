"""
Square supplies
===============

With the zombie cure injections ready to go, it’s time to start treating our zombified rabbit friends (known as zombits) at our makeshift zombit treatment center. You need to run out really fast to buy some gauze pads but you only have 30 seconds before you need to be back.

Luckily, the corner store has unlimited gauze pads in squares of all sizes. Jackpot! The pricing is simple – a square gauze pad of size K x K costs exactly K * K coins. For example, a gauze pad of size 3×3 costs 9 coins.

You’re in a hurry and the cashier takes a long time to process each transaction. You decide the fastest way to get what you need is to buy as few gauze pads as possible, while spending all of your coins (you can always cut up the gauze later if you need to). Given that you have n coins, what’s the fewest number of gauze pads you can buy?

Write a method answer(n), which returns the smallest number of square gauze pads that can be bought with exactly n coins.

n will be an integer, satisfying 1 <= n <= 10000.

Test cases
==========

Inputs:
(int) n = 24
Output:
(int) 3

Inputs:
(int) n = 160
Output:
(int) 2
"""

import math

def answer(n, md=None):

    # md is Max Depth
    # after thsi depth, there is already a better known solution

    upper = int(math.sqrt(n))

    i = upper

    # if md is not defined, find the naive answer (usually best)
    # subtract the biggest possible square number
    if md == None:
        k = 0
        j = n
        
        while True:
            j = j - i**2
            k += 1
            if j == 0:
                break
            else:
                while True:
                    if i**2 > j:
                        i -= 1
                    else:
                        break

        md = k

    # n = 0, 1, 2, 3 have result 0, 1, 2, 3
    if n <= 3:
        return n
    # if md = 0 we are too deep, not a better solution
    if md == 0:
        return 9999
    # upper bound is rounded up sqrt(n)
    upper = int(math.sqrt(n))
    i = upper
    # lower bound is point where i^2 * max depth is > n
    while True:
        if md * i**2 < n:
            break
        i -= 1
    lower =  i + 1
    l = []
    for i in range(lower, upper+1):
        l.append(answer(n - i**2, md=md-1)+1)
    # if l is empty, no better solutions exist
    if l == []:
        return 9999
    else:
        return min(l)


print answer(24)
print answer(160)
print answer(12)


#for i in range(10000):
#    print "%s %s" % (10000-i, answer(i) )
