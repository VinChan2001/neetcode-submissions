class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R= 0, len(s)-1

        while L<R:
            s[R],s[L]=s[L],s[R]
            L+=1
            R-=1
        return s

            



        