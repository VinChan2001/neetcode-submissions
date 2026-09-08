class Solution:
    def validPalindrome(self, s: str) -> bool:
        #optimal solution
        def check(L, R):
            while L< R:
                if s[L] != s[R]:
                    return False
                L+=1
                R-=1
            return True
        
        L=0
        R=len(s)-1
        while L<R:
            if s[L]==s[R]:
                L+=1
                R-=1
            else:
                return check(L+1, R) or check(L, R-1)
        
        return True

            


        