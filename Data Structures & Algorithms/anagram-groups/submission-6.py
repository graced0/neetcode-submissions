class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #aiming for 0(m*n) which means solution should be found after iterating through each char of each word
        
        hashmap = defaultdict(list) # key -> freq of chars, value -> word that fits in key
        for word in strs:
            hashmap[tuple(sorted(word))].append(word)

        return list(hashmap.values())  # have to use list() as .values() returns read only view object
            
