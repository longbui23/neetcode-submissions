class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for word in words:
            for char in word:
                indegree[char] = 0

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            m, n = len(word1), len(word2)

            if m > n and word1[:min(m,n)] == word2[:min(m,n)]:
                return ""

            for j in range(min(m, n)):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].append(word2[j])
                        indegree[word2[j]] += 1
                    break

        
        res = []
        q = deque([c for c in indegree if indegree[c] == 0])
        while q:
            char = q.popleft()
            res.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegree):
            return ""
        return "".join(res)

        


                

            