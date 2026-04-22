class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        map_one, map_two = defaultdict(int), defaultdict(int)
        for num in range(len(s)):
            map_one[s[num]] += 1
            map_two[t[num]] += 1

        return map_one == map_two
