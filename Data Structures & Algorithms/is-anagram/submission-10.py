class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #must have the same number of chars to ever return true
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for n in range(len(s)):
            count[s[n]] += 1
            count[t[n]] -= 1

        return all(v == 0 for v in count.values())
