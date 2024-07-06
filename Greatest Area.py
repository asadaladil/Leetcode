def maxArea(A):
    a=0
    b=len(A)-1
    mx=-100
    while a!=b:
        area=min(A[a],A[b])*(b-a)
        mx=max(mx,area)
        if A[a]<A[b]:
            a+=1
        else:
            b-=1
    return mx
   

A=list(map(int,input().split()))
print(maxArea(A))
# Algorithm note Faang queation 2(Leetcode->Container with water)
