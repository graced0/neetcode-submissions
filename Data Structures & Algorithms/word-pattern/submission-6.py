class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False


        char_word = {}
        word_char = {}

        for word, char in zip(pattern, words):
            if char in char_word: #if we have seen this char already
                if char_word[char] != word:
                    return False
            else: 
                if word in word_char: #if we haven't seen this char, but we have seen this word
                    return False
                else:
                    char_word[char] = word
                    word_char[word] = char

        return True


