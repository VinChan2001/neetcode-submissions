class Solution:
    def isValid(self, s: str) -> bool:
        dictMap = {']': '[', '}': '{', ')': '('}
        stack = []

        for i in s:
            if i in dictMap:
                if stack and stack[-1]==dictMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
            
        