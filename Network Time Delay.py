import heapq
def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    inf=1000
    weight=[inf]*(n+1)
    weight[0]=0
    visited=[0]*(n+1)
    visited[0]=1
    Graph={}
    for i in times:
        if i[0] in Graph:
            Graph[i[0]].append((i[1],i[2]))
        else:
            Graph[i[0]]=[(i[1],i[2])]

    for i,j in Graph.items():
        print(f"{i}:{j}")

    def Dijkstra(start):
        queue=[]
        heapq.heappush(queue,(0,start))
        weight[start]=0
        while queue:
            u=heapq.heappop(queue)[1]
            if visited[u]==1:
                continue
            if u not in Graph:
                visited[u]=1
                continue
            for (v,w) in Graph[u]:
                if w+weight[u]<weight[v]:
                    weight[v]=w+weight[u]
                heapq.heappush(queue,(weight[v],v))
            visited[u]=1
        if visited.count(1)==n+1:
            return max(weight)
        return -1
    return Dijkstra(k)

        

print(networkDelayTime([[1,2,9],[1,4,2],[4,2,4],[4,5,6],[2,5,1],[5,3,7],[3,1,5],[3,2,3]],5,1))
#print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
