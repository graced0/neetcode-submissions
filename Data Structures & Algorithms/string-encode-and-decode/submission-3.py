class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for st in strs:
            encoded_string.append(str(len(st)))
            encoded_string.append("#")
            encoded_string.append(st)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0

        while i < len(s):
            #j = s.find('#', i) #finds first instance of '#' starting from index i

            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            string = s[j + 1:j + 1 + length]
            decoded_strings.append(string)
            i = j + 1 + length
            

        return decoded_strings