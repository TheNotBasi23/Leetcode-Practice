from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        arrLand = [(i,j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1]
        land = set(arrLand)
        queueOfLand = deque(arrLand)
        largestSectionOfLand = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while land:
            seed = land.pop()
            island = deque([seed])
            size = 1
            while island:
                seedValueRow,seedValueCol = island.popleft()
                potentialMoves = [(seedValueRow + l,seedValueCol + r) for l,r in directions]
                for element in potentialMoves:
                    if element in land:
                        size +=1
                        land.remove(element)
                        island.append(element)
            largestSectionOfLand = max(largestSectionOfLand,size)
        return largestSectionOfLand


