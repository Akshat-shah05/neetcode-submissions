class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for p in s:
            if p not in matches:
                stack.append(p)
            
            elif p in matches:
                if not stack:
                    return False
                corresponding = stack.pop()
                if corresponding != matches[p]:
                    return False
        
        return True if not stack else False
        