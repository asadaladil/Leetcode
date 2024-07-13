
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
    m = len(grid)
    n=len(grid[0])
    island=0

    def valid(i,j):
        if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]):
            return True
        return False
    
    def DFS(i,j):
        if grid[i][j]=='1':
            grid[i][j]='0'
        if valid(i-1,j) and grid[i-1][j]=='1':
            DFS(i-1,j)
        if valid(i,j+1) and grid[i][j+1]=='1':
            DFS(i,j+1)
        if valid(i+1,j) and grid[i+1][j]=='1':
            DFS(i+1,j)
        if valid(i,j-1) and grid[i][j-1]=='1':
            DFS(i,j-1) 
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                island+=1
                DFS(i,j)
    return island

print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))