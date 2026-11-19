class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in mapping:
                if not stack:
                    return False
                
                top = stack.pop()

                if mapping[i] != top:
                    return False

        return len(stack) == 0