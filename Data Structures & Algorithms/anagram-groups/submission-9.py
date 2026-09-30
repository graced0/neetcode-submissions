class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            counter = [0] * 26
            for char in string:
                counter[ord('a') - ord(char)] += 1
            anagrams[tuple(counter)].append(string)

        return list(anagrams.values())
            
            
