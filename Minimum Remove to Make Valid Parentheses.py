def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    arr={
        '(':[],
        ')':[]
    }
    arr2=[]
    for i in range(len(s)):
        if s[i]=='(' or s[i]==')':
            arr[s[i]].append(i)
        if s[i]=='(':
            arr2.append(s[i])
        elif len(arr2)>0 and s[i]==')' and arr2[-1]=='(':
            arr2.pop()
            if len(arr['(']) and len(arr[')']):
                arr[')'].pop()
                arr['('].pop()
    res=""
    for i in range(len(s)):
        if i not in arr['('] and i not in arr[')']:
            res+=s[i]
    return res

x=input()
print(minRemoveToMakeValid(x))
