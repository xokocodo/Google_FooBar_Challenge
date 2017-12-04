def answer(t, n, p=0):
    # t = number of rolls allowed
    # n = number of spaces on the board
    # p = current space on the board selected (defaults to zero, which corresponds to the first space)
    # p can also be thought of as the number of backwards moves allowed before hitting the edge
    # note: without p, there wouldn't be a way to tell if the path takes us too far to the left

    # memoization
    # if no table exists, create table
    # if table exists, check table for previous answer
    if not hasattr(answer, "table"):
        answer.table = {}
    elif answer.table.get((t, n, p)) != None:
        return answer.table.get((t, n, p))

    # if p < 0, marker has gone off board, the game is invalid
    if p < 0:
        return 0
    # if rolls left is less than forward jumps needed, the game is impossible
    elif t < n - 1:
        return 0
    # if the rolls left is equal to the forward jumps needed, only one game is possible
    elif t == n - 1:
        return 1
    # if there is only one space on the board, there is only one possible game
    # note: this prevents games from going past the end of the board or going
    # back after reaching the last square
    if n == 1:
        return 1
    # Recursively calculate the number of options for each possibile next roll (back, stay, forward)
    # Each move decreses t (number of future rolls allowed)
    # Going forward decreases n (which is anologous to playing the game on a smaller board) and increases p
    # Going backwards increases n (which is analogous to playing on a larger board) and decreases p
    # Staying in the same square leaves n and p the same
    # These answers are then added together and the modulo 123454321 is taken
    else:
        # note: (a+b+c)%d == (a%d + b%d + c%d) % d
        # this allows us to store the result mod 123454321 and recursively add them back together
        # instead of getting the complete answer, and only then taking the modulo.
        result = (answer(t-1, n+1, p-1) + answer(t-1, n, p) + answer(t-1, n-1, p+1)) % 123454321
        # Add the new result to the table
        answer.table[(t, n, p)] = result
        return result
    
import time

start = time.time()

print answer(1, 2) == 1
print answer(3, 2) == 3
print answer(5, 4)
print answer(900, 4)
print answer(800, 8)
print answer(700, 12)
print answer(600, 16)
print answer(500, 20)
print answer(400, 24)
print answer(300, 28)
print answer(200, 32)
print answer(100, 36)

end = time.time()

print "%s seconds elapsed time" % ( end - start )
