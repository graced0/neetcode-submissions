class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        hashmap = {}
        res = []
        for i, char in enumerate(pattern):
            if char in hashmap:
                if hashmap[char] != words[i]:
                    return False
            else:
                if words[i] in hashmap.values():
                    return False
                hashmap[char] = words[i]
            res.append(char)

        print("".join(res))
        return "".join(res) == pattern


