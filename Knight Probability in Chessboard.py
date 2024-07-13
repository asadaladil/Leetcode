def knightProbability(n, k, row, column):
    """
    :type n: int
    :type k: int
    :type row: int
    :type column: int
    :rtype: float
    """
    if k==0:
        return 1.0000
    if n==0:
        return 0.0000
    Direction=[[1,-2],[1,2],[-2,1],[2,1],[-2,-1],[-1,-2],[-1,2],[2,-1]]
    memory={}

    def Dynamic(k,r,c):
        # Memoization method.....
        
        if r<0 or r>=n or c<0 or c>=n:
            return 0
        if k==0:
            return 1
        if (k,r,c) in memory:
            return memory[(k,r,c)]
        for i in Direction:
            if (k,r,c) not in memory:
                memory[(k,r,c)]=Dynamic(k-1,r+i[0],c+i[1])
            else:
                memory[(k,r,c)]+=Dynamic(k-1,r+i[0],c+i[1])
        return memory[(k,r,c)]

    return Dynamic(k,row,column)/8**k 

print(knightProbability(3,3,0,0))