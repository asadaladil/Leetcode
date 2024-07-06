def original(s):
    n=len(s)
    res=""
    for i in range(n):
        if s[i]=='#' and len(res)>0:
            res=res[:-1]
        else:
            res+=s[i]
    return res

x,y=input().split()
print(original(x)==original(y))