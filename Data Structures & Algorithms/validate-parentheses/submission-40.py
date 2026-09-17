class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{", ")":"(", "]":"["}
        stack = []
        for i in s:
            if i in d:
                if len(stack)>0 and stack[-1]==d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False 



        