class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        heap = [(grid[0][0],0,0)]
        visited = set([(0,0)])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while heap:
            time, curr_x, curr_y = heapq.heappop(heap)
            if curr_x == m - 1 and curr_y == n - 1:
                return time

            for dx,dy in dirs:
                new_x, new_y = curr_x + dx, curr_y + dy
                if (
                    0 <= new_x < m and 
                    0 <= new_y < n and 
                    (new_x, new_y) not in visited
                ):
                    visited.add((new_x, new_y))
                    heapq.heappush(
                        heap, (
                            max(time, grid[new_x][new_y]),
                            new_x, new_y
                        )
                    )

        return -1


                