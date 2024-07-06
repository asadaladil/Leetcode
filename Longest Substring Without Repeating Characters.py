
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    s.replace(' ',"00")
    n=len(s)
    res=[]
    l=0
    r=0
    mx=0
    while r!=n and n>0:
        if s[r] in res:
            res.remove(s[l])
            l+=1
        else:
            res.append(s[r])
            mx=max(mx,r-l+1)
            r+=1
    return mx

x=input()
print(lengthOfLongestSubstring(x))