class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(m * n) means we need to visit every char in every string
        hashmap = defaultdict(list) #hashmap in which values are defaulted as an empty list
        for st in strs: #for each st in strs
            counter = [0] * 26 #create a counter for each character
            for char in st:
                counter[ord('a') - ord(char)] += 1 #increment counter for each char
            hashmap[tuple(counter)].append(st) #append st to keys with matching chars (anagrams)
        return list(hashmap.values()) #return the values of the list (list of grouped anagrams)
            
