class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_one, freq_two = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            freq_one[s[i]] += 1
            freq_two[t[i]] += 1

        return freq_one == freq_two;
