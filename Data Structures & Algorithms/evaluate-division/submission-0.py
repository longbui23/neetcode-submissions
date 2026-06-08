class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hsh = defaultdict(list) 

        for i, eq in enumerate(equations):
            a, b = eq
            hsh[a].append((b, values[i]))
            hsh[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in hsh or target not in hsh:
                return -1
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nei, weight in hsh[node]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]