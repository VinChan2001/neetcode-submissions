class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if i.isalnum():
                r+=i.lower()
        
        L=0
        R=len(r)-1

        while L<R:
            if r[L]!=r[R]:
                return False
            L+=1
            R-=1
        
        return True

        