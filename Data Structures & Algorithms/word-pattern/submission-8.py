class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False


        char_word = {}
        word_char = {}

        for word, char in zip(pattern, words):
            if char in char_word and char_word[char] != word: #if char has been seen, but char -> word doesn't match current
                    return False
            if word in word_char and word_char[word] != char: #if word has been seen, but word -> char doesn't match current
                    return False
            char_word[char] = word
            word_char[word] = char

        return True


