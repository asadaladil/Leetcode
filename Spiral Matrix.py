

def is_valid(m,n,i,j):
    if i>=0 and i<m and j>=0 and j<n:
        return True
    return False

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    arr=[len(matrix),len(matrix[0])]
    List=[]
    i,j=0,0
    a=1
    b=1
    while True:
        if matrix[i][j]!=-1000:
            List.append(matrix[i][j])
            matrix[i][j]=-1000
        if abs(a+b)==2:
            if is_valid(arr[0],arr[1],i,j+b) and matrix[i][j+b]!=-1000:
                j+=b
            else:
                b*=-1
        if (a+b)==0:
            if is_valid(arr[0],arr[1],i+a,j) and matrix[i+a][j]!=-1000:
                i+=a
            else:
                a*=-1
        if (len(List)==arr[0]*arr[1]):
            break
    return List

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
            