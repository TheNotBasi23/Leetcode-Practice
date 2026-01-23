from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting = deque()
        oranges = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    oranges.add((i,j))
                elif grid[i][j] == 2:
                    rotting.append((i,j))
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        numToProccess = len(rotting)
        count = 0
        layer = -1
        while rotting:
            item = rotting.popleft()
            count += 1
            potentialCandidates = [
                (item[0] + l,item[1] + r) for l,r in dir
                if (item[0] + l,item[1] + r) in oranges
            ]
            for item in potentialCandidates:
                rotting.append(item)
                oranges.remove(item)
            if count == numToProccess:
                numToProccess = len(rotting)
                count = 0
                layer +=1

        if oranges:
            return -1
        else:
            return layer if layer != -1 else 0
print(Solution().orangesRotting(grid = [[0,2]]
))



