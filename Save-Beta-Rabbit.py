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