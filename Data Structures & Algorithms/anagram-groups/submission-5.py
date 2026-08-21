class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #aiming for 0(m*n) which means solution should be found after iterating through each char of each word
        
        hashmap = defaultdict(list) # key -> freq of chars, value -> word that fits in key
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord('a')] += 1 # ord() returns unicode value
            hashmap[tuple(counter)].append(word)

        return list(hashmap.values())  # have to use list() as .values() returns read only view object
            
