from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        exits = set()
        n = len(maze)
        m = len(maze[0])
        visited = set()
        for i in range(m):
            if maze[0][i] == ".":
                exits.add((0,i))
            if maze[n-1][i] == ".":
                exits.add((n-1,i))
        for i in range(1,len(maze) - 1):
            if maze[i][0] == ".":
                exits.add((i,0))
            print(n-1)
            if maze[i][m - 1] == ".":
                exits.add((i,m-1))
        if (entrance[0],entrance[1]) in exits:
            exits.remove((entrance[0],entrance[1]))

        q = deque()
        q.append((entrance[0],entrance[1]))
        count = 0
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        itemsToProcess = len(q)
        visited.add((entrance[0],entrance[1]))
        layer = 0
        while q:
            itemL,itemR = q.popleft()
            if (itemL,itemR) in exits:
                return layer
            count +=1
            potenitalCandidates = [(itemL + l,itemR + r) for l,r in dir if 0 <= itemL + l < n and 0<= itemR + r < m  and (itemL + l,itemR + r) not in visited and maze[itemL + l][itemR + r] == "." ]

            for element in potenitalCandidates:
                q.append(element)
                visited.add(element)
            if count == itemsToProcess:
                itemsToProcess = len(q)
                count = 0
                layer +=1

        return -1

print(Solution().nearestExit(maze = [["."],["."],["."],["."]], entrance = [2,0]))