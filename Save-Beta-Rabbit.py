#Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through this grid and feed the zombies.

#Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above, below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

#To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food as possible at the end.

#Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

#food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

#grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.

#The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.

def answer(food, grid):
    N = len(grid)
    if N == 1:
	    if food - grid[0][0] > 0:
	        return food - grid[0][0]
	    else:
	        return -1
        
    down = [set([grid[0][1]])]
    across = [set([grid[1][0]])]
    corner = [set([grid[1][1]+grid[0][1],grid[1][1]+grid[1][0]])]
    
    def crossAdd(list1, list2):
	    new = []
	    for num1 in list1:
	        for num2 in list2:
	            if num1+num2 not in new and num1 + num2 <= food:
	                new.append(num1 + num2)
	    return set(new)
	
    def doit(level):
	    down[0] = crossAdd(down[0], [grid[0][level+1]])
	    across[0] = crossAdd(across[0], [grid[level+1][0]]) 
	    for i in range(1,level):
	        down[i] = crossAdd(down[i], [grid[i][level+1]]) | crossAdd(down[i], down[i-1])
	        across[i] = crossAdd(across[i], [grid[level+1][i]]) | crossAdd(across[i], across[i-1])
	    down.append(crossAdd(corner[0], [grid[level][level+1]]))
	    down[level] = down[level] | crossAdd([grid[level][level+1]], down[level-1])
	    across.append(crossAdd(corner[0], [grid[level+1][level]]))
	    across[level] = across[level] | crossAdd([grid[level+1][level]], across[level-1])
	    corner[0] = crossAdd([grid[level+1][level+1]],down[level]) | crossAdd([grid[level+1][level+1]],across[level])
	
    level = 1
    while level < N - 1:
	    doit(level)
	    level += 1
	    

    results = list(corner[0])
    offset = 0
    for i in range(len(results)):
	    results[i-offset] = food - results[i-offset]
	    if results[i-offset] < 0 :
		    del results[i-offset]
		    offset += 1
    results.sort()
    if len(results) == 0:
	    return -1
    else:
	    return results[0]
	    
print answer(1, [[0]])
print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
