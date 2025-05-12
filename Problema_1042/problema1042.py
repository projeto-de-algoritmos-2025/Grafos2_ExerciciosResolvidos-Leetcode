class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        flowers = [0] * n

        for i in range(n):
            used = set()
            for nei in graph[i]:
                if flowers[nei] != 0:
                    used.add(flowers[nei])

            for color in range(1, 5):
                if color not in used:
                    flowers[i] = color
                    break

        return flowers
