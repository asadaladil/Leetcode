
# Unable to judge the code in leetcode as subscription needed
def isValid(i,j,m,n):
    if i>=0 and i<m and j>=0 and j<n:
        return True
    return False

def walls_and_gate(matrix):
    if not matrix:
        return matrix
    m,n=len(matrix),len(matrix[0])
    gate=[]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                gate.append([i,j])


    def DFS(i,j,count=0):
        if not isValid(i,j,len(matrix),len(matrix[0])) or matrix[i][j]<count:
            return
        matrix[i][j]=count
        DFS(i+1,j,count+1)
        DFS(i-1,j,count+1)
        DFS(i,j+1,count+1)
        DFS(i,j-1,count+1)
    
    for i in gate:
        DFS(i[0],i[1])
    return matrix

inf=2147483647
matrix=walls_and_gate([[inf,-1,0,inf],[inf,inf,inf,-1],[inf,-1,inf,-1],[0,-1,inf,inf]])
for i in matrix:
    print(i)