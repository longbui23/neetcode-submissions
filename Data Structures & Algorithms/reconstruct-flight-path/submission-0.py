class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        res = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)

        dfs("JFK")
        return res[::-1]