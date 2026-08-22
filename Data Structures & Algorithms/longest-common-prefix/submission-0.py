class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        for s in strs[1:]:
            while check not in s:
                check = check[:-1]
        return check

            
