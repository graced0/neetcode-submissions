class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            count = [0] * 26 # array of 26 zeros

            for character in string:
                count[ord(character) - ord('a')] += 1 # incrementing the counter for each character found

            result[tuple(count)].append(string)
        return result.values()
            
        #count: a list of 26 values, each used to count the number of times a specific letter is found
        # e.g. "abc" = [1],[1],[1],[0]... or "aabc" = [2],[1],[1],[0]...
        #result is a hashmap of keys of various count[...] with values of their corresponding word
        #since each anagram will have the same count[...], calling the values will group strings that are anagrams together