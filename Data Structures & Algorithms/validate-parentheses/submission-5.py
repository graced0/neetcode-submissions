class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close_map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in open_close_map:
                if stack and stack[-1] == open_close_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack