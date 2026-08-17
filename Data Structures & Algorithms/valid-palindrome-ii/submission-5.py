class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            k = list(s)
            k[i] = ''
            
            if ''.join(k) == ''.join(k[::-1]):
                return True
            k = list(s)
        return False

        