def numOfMinutes(n, headID, manager, informTime):
    """
    :type n: int
    :type headID: int
    :type manager: List[int]
    :type informTime: List[int]
    :rtype: int
    """
    Graph={}
    for i in range(n):
        if manager[i]==-1:
            continue
        if manager[i] in Graph:
            Graph[manager[i]].append(i)
        else:
            Graph[manager[i]]=[i]

    
    mx=[-10]
    def DFS(i,count):
        if i in Graph:
            for k in Graph[i]:
                DFS(k,count+informTime[k])
        mx[0]=max(mx[0],count)
        return mx[0]
    
    return DFS(headID,informTime[headID])

print(numOfMinutes(8,4,[2,2,4,6,-1,4,4,5],[0,0,4,0,7,3,6,0]))
#print(numOfMinutes(1,0,[-1],[0]))