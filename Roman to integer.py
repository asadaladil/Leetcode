def romanToInt(s):
    mp={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    res=mp[s[-1]]
    for i in range(len(s)-2,-1,-1):
        if mp[s[i]]<mp[s[i+1]]:
            res-=mp[s[i]]
        else:
            res+=mp[s[i]]
    return res