import heapq

class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        if m > 1 and grid[1][0] > 1 and n > 1 and grid[0][1] > 1:
            return -1

        heap = [(0, 0, 0)]
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    arrive = t + 1
                    wait_time = grid[nr][nc]
                    if arrive < wait_time:
                        arrive = wait_time + ((wait_time - arrive) % 2)

                    if arrive < visited[nr][nc]:
                        visited[nr][nc] = arrive
                        heapq.heappush(heap, (arrive, nr, nc))

        return -1
