
def vowel(s):
    for i in s:
        if i == 'a'or'e'or'i'or'o'or'u':
            ans = i
    return ans

def ispalindrome(s):
    a =[]
    a = s[::-1]
    for i in range(0,len(s)):
        if s[i] == a[i]:
            return True
        else:
            return False

def issymmetrical(s):
    start =0
    n= len(s)
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
    while(start<mid and mid<n):
        if s[start] == s[mid]:
            return True
        else:
            return False     

def isvowelpalindrome(s):
    a = vowel(s)
    b =[]
    b = a[::-1]
    for i in range(0,len(s)):
        if a[i] == b[i]:
            return True
        else:
            return False

s = input("Enter a String: ")
if ispalindrome(s):
    print("it is a palindrome")
else:
    print("it is not a palindrome")

if issymmetrical(s):
   print("it is a symmetrical")
else:
   print("it is not a symmetrical")

if isvowelpalindrome(s):
    print("it is a vowelpalindrome")
else:
    print("it is not a vowelpalindrome")
