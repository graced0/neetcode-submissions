class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for st in strs:
            counter = [0] * 26
            for char in st:
                counter[ord('a') - ord(char)] += 1
            hashmap[tuple(counter)].append(st)
        return list(hashmap.values())
            
