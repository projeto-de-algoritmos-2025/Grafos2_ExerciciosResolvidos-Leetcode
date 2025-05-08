import heapq
from collections import defaultdict

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))

        heap = [(0, src, 0)]

        visited = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue

            visited[(city, stops)] = cost

            if stops <= k:
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1
    