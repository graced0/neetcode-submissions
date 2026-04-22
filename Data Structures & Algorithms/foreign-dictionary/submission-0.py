class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { char : set() for word in words for char in word }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            #invalid base case, word that is a prefix of another word comes earlier in sort
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {} # not in map = unvisited, false = visited, true = current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char] #will return false if alr visited, true if there is a cycle/loop

            visited[char] = True
            for a in adj[char]:
                if dfs(a):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)