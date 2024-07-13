
def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
        return 0
    m, n = len(grid),len(grid[0])
    fresh =[0]
    rotten=[]
    for i in range (m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh[0]+=1
            if grid[i][j]==2:
                rotten.append([i,j])
    
    def valid(i,j):
        if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]):
            return True
        return False
    def DFS(i,j):
        do_rotten=[]
        if valid(i,j+1) and grid[i][j+1]==1:
            grid[i][j+1] = 2
            fresh[0]-=1
            do_rotten.append([i,j+1])
        if valid(i-1,j) and grid[i-1][j]==1:
            grid[i-1][j] = 2
            fresh[0]-=1
            do_rotten.append([i-1,j])
        if valid(i+1,j) and grid[i+1][j]==1:
            grid[i+1][j] = 2
            fresh[0]-=1
            do_rotten.append([i+1,j])
        if valid(i,j-1) and grid[i][j-1]==1:
            grid[i][j-1] = 2
            fresh[0]-=1
            do_rotten.append([i,j-1])
        return do_rotten
    minutes=0
    while rotten:
        do_rotten=[]
        for i in rotten:
            x=DFS(i[0],i[1])
            if x:
                do_rotten.extend(x)
        rotten=do_rotten
        if rotten:
            minutes+=1
    if fresh[0]>0:
        return -1
    return minutes

print(orangesRotting([[0,2]]))
        