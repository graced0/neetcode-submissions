class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        want_count = {} 
        window = {}

        for char in t:
            want_count[char] = 1 + want_count.get(char, 0)

        have = 0
        need = len(want_count)

        res = [-1, -1]
        res_len = float("inf")

        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in want_count and window[char] == want_count[char]:
                have += 1

            while have == need:
                #update best result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)
                
                #move left pointer and update count
                window[s[left]] -= 1
                if s[left] in want_count and window[s[left]] < want_count[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float("inf") else ""

