from collections import deque

class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        
        color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len([x for x in graph[c] if x != 0])  
        
        q = deque()

        for i in range(n):
            for turn in range(2):
                if i != 0:
                    color[0][i][turn] = MOUSE_WIN
                    q.append((0, i, turn, MOUSE_WIN))
                    color[i][i][turn] = CAT_WIN
                    q.append((i, i, turn, CAT_WIN))

        while q:
            m, c, turn, result = q.popleft()
            prev_turn = 1 - turn
            if prev_turn == 0:  
                for pm in graph[m]:
                    if color[pm][c][prev_turn] == DRAW:
                        if result == MOUSE_WIN:
                            color[pm][c][prev_turn] = MOUSE_WIN
                            q.append((pm, c, prev_turn, MOUSE_WIN))
                        else:
                            degree[pm][c][prev_turn] -= 1
                            if degree[pm][c][prev_turn] == 0:
                                color[pm][c][prev_turn] = CAT_WIN
                                q.append((pm, c, prev_turn, CAT_WIN))
            else:
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if color[m][pc][prev_turn] == DRAW:
                        if result == CAT_WIN:
                            color[m][pc][prev_turn] = CAT_WIN
                            q.append((m, pc, prev_turn, CAT_WIN))
                        else:
                            degree[m][pc][prev_turn] -= 1
                            if degree[m][pc][prev_turn] == 0:
                                color[m][pc][prev_turn] = MOUSE_WIN
                                q.append((m, pc, prev_turn, MOUSE_WIN))

        return color[1][2][0]
