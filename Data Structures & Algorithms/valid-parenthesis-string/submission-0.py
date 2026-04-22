class Solution:
    def checkValidString(self, s: str) -> bool:
        close_max = 0
        close_min = 0
        for char in s:
            if char == '(':
                close_max += 1
                close_min += 1
            elif char == ')':
                close_max -= 1
                close_min -= 1
            else:
                close_max += 1
                close_min -= 1
            if close_max < 0:
                return False
            if close_min < 0:
                close_min = 0

        return close_min == 0
