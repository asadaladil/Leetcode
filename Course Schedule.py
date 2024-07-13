def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    inDegree=[0]*numCourses
    adj_list={}
    for i in prerequisites:
        if i[1] in adj_list:
            adj_list[i[1]].append(i[0])
        else:
            adj_list[i[1]]=[i[0]]
        inDegree[i[0]]+=1

    for i,j in adj_list.items():
        print(f"{i}:{j}")
    print(inDegree)
    
    while True:
        if len(adj_list)==0:
            return True
        if 0 in inDegree:
            index=inDegree.index(0)
            inDegree[index]=-1
            if index in adj_list:
                for i in adj_list[index]:
                    inDegree[i]-=1
                adj_list.pop(index)
        else:
            return False
        


print(canFinish(6,[[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]))
#print(canFinish(2,[[1,0],[0,1]]))
