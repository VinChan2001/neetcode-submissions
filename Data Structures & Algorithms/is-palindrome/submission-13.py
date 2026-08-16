class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split(' ')
        z=''
        for i in s:
            z+=i.lower()
        k=''
        for i in z:
            if i.isalnum():
                k+=i
        return k==k[::-1]

        

