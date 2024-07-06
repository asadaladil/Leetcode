def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    res=""
    for i in s:
        if i>='a' and i<='z' or i>='A' and i<='Z' or i>='0' and i<='9':
            res+=i
    res=res.lower()
    print(res)
    return res==res[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))