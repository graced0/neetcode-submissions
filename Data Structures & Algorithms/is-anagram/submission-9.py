class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #must have the same number of chars to ever return true
        if len(s) != len(t):
            return False

        freq_one, freq_two = defaultdict(int), defaultdict(int)

        for n in range(len(s)):
            freq_one[s[n]] += 1
            freq_two[t[n]] += 1

        return freq_one == freq_two
