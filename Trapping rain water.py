#leetcode

def trap(height):
    n=len(height)
    Lmax=height[0]
    Rmax=height[n-1]
    l=0
    r=n-1
    res=0
    while l!=r:
        if Lmax<Rmax:
            l+=1
            res+=max(0,Lmax-height[l])
            Lmax=max(Lmax,height[l])
        else:
            r-=1
            res+=max(0,Rmax-height[r])
            Rmax=max(Rmax,height[r])
    return res

A=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(A))