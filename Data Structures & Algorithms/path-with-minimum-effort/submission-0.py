class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        heap = [(0, 0,0)]
        heapq.heapify(heap)
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()

        while heap:
            effort, i, j = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return effort
            if (i, j) in visited:
                continue
            
            visited.add((i,j))
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_effort = max(effort, abs(heights[i][j] - heights[ni][nj]))
                    heapq.heappush(heap, (new_effort, ni, nj))

        return -1
            
            