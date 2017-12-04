# Carrotland
# ==========
# The rabbits are free at last, free from that horrible zombie science
# experiment. They need a happy, safe home, where they can recover.
# You have a dream, a dream of carrots, lots of carrots, planted in neat
# rows and columns! But first, you need some land. And the only person
# who's selling land is Farmer Frida. Unfortunately, not only does she
# have only one plot of land, she also doesn't know how big it is - only
# that it is a triangle. However, she can tell you the location of the
# three vertices, which lie on the 2-D plane and have integer coordinates.
# Of course, you want to plant as many carrots as you can. But you also
# want to follow these guidelines: The carrots may only be planted at
# points with integer coordinates on the 2-D plane. They must lie within
# the plot of land and not on the boundaries. For example, if the vertices
# were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at
# (0,0).
# Write a function answer(vertices), which, when given a list of three
# vertices, returns the maximum number of carrots you can plant.
# The vertices list will contain exactly three elements, and each element
# will be a list of two integers representing the x and y coordinates of a
# vertex. All coordinates will have absolute value no greater than
# 1000000000. The three vertices will not be collinear.
# Test cases
# ==========
# Inputs:
    # (int) vertices = [[2, 3], [6, 9], [10, 160]]
    # [(1, 2), (5, 8), (9, 159)]
# Output:
    # (int) 289
# Inputs:
    # (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
# Output:
    # (int) 1730960165

import math

# Returns list of factors of n
def factor(n):
    r = []

    # Check up to sqrt(n) for factors
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            r.append(i)
            n = n / i
            # Recursively check for additional factors
            r += factor(n)
            break
                
    if r == []:
        r = [n]
       
    return r

# Returns the number of points on a grid that the line
# segment with delta x and delta y intersects in its path
# Note: the result only include one of the extreme edge points
# of the line. The other point will be captured in the next boundary
def boundary(del_x, del_y):

    # Note: this function is symetrical with it's arguments
    # e.g. boundary(A,B) = boundary(B,A)

    # If either one is 0 the number of points
    #intersected is just the other one's value
    if del_x == 0:
        return del_y

    if del_y == 0:
        return del_x

    # Factor both delX and delY
    fact_x = factor(del_x)
    fact_y = factor(del_y)

    # Simplify the fraction by removing factors
    # in factX that also exist in factY
    for f in fact_x:
        if f in fact_y:
            fact_y.remove(f)

    # Now that the faction is simplied as much as possible
    # we now multiply out the factors to find the simplified
    # denomenator value

    product = 1
    for f in fact_y:
        product = product * f

    # The orginal value divded by the simplifed value tells us how many time
    # simplified value fits in the orginal value, which gives us the number of
    # interections on the grid

    return del_y/product


def answer(vertices):

    # Use Pick's Theroum Which Deals With Points Inside Polygons
    # A = i + b/2 - 1
    # Where A is area, i are points inside, and b are points on the boundaries
    # i = A - b/2 + 1

    # Note: This answer is generalized to accept any 2D polygon
    # However in the case of this challenge n will always be 3 (triangle)
    n = len(vertices)

    # Find A
    # Use the Shoelace formula to find the area using the vertices
    s = 0
    for i in range(n-1):
        s += vertices[i][0] * vertices[i+1][1]
    s += vertices[n-1][0] * vertices[0][1]
    for i in range(n-1):
        s -= vertices[i+1][0] * vertices[i][1]
    s -= vertices[0][0] * vertices[n-1][1]
    A = 0.5 * abs(s)

    # Find b
    b = 0
    # Check each boundary (edge of the polygon) for points intersected on the grid
    for i in range(n-1):
        b += boundary(abs(vertices[i][0]-vertices[i+1][0]), abs(vertices[i][1]-vertices[i+1][1]))
    b += boundary(abs(vertices[n-1][0]-vertices[0][0]), abs(vertices[n-1][1]-vertices[0][1]))

    # Pick's Theroum
    return int(A - b/2 + 1)

"""
vertices = [[0, 0], [0, 5], [5, 0]]
print answer(vertices) #6

vertices = [[2, 3], [6, 9], [10, 160]]
print answer(vertices) #289

vertices = [[91207, 89566], [-88690, -83026]
            , [67100, 47194]]
print answer(vertices) #1730960165
"""
