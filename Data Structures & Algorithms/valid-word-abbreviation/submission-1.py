class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0
        while l < len(word) and r < len(abbr):
            if word[l] == abbr[r]:
                l, r = l + 1, r + 1
            elif abbr[r] == "0" or abbr[r].isalpha():
                return False
            else:
                startInd = r
                while r < len(abbr) and not abbr[r].isalpha():
                    r += 1
                l += int(abbr[startInd:r])

        return l == len(word) and r == len(abbr)
