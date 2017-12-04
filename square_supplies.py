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
