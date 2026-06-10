class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * n

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
            degree[k] += 1
            degree[v] += 1


        q = deque([i for i in range(n) if degree[i] == 1])
        visited = set()

        while q:
            if n <= 2:
                break
        
            size = len(q)
            n -= size
            for i in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q) if len(q) > 0 else [0]
                

