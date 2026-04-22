class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpenMap = {")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in closeOpenMap:
                if stack and stack[-1] == closeOpenMap[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else: 
            return False