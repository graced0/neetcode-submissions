class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        one, two = [0] * 26, [0] * 26
        for i in range(len(s)):
            one[ord('a') - ord(s[i])] += 1
            two[ord('a') - ord(t[i])] += 1
        return one == two

