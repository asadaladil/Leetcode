def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    cost.append(0)
    memory={}
    def Dynamic(i):
        # Memoization method:

        # if i<0:
        #     return 0
        # if i in memory:
        #     return memory[i]
        # memory[i]=cost[i]+min(Dynamic(i-1),Dynamic(i-2)) # Top down Approach
        # return memory[i]

        # Tabulation method:

        n=len(cost)
        memory={}
        for i in range(n):
            if i<2:
                memory[i]=cost[i]
                continue
            memory[i]=cost[i]+min(memory[i-1],memory[i-2])
        return min(memory[n-1],memory[n-2])

        # Tabulation method optimized:
        # n=len(cost)
        # dp1=cost[0]
        # dp2=cost[1]
        # for i in range(2,n):
        #     dp1,dp2=dp2,cost[i]+min(dp1,dp2)
        # return min(dp1,dp2)

    
    return Dynamic(len(cost)-1)

print(minCostClimbingStairs([10,15,20]))
#print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))