from collections  import  deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        elements = [(i,j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "1"]
        setOfLand = set(elements)
        q = deque(elements)
        counter = 0
        while setOfLand:
            seed = q.popleft()
            while seed not in setOfLand:
                seed = q.popleft()
            myQueue = deque([seed])
            while myQueue:
                itemToExpand = myQueue.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                validMoves = [(itemToExpand[0] + direction[0],itemToExpand[1] + direction[1])
                              for direction in directions if (itemToExpand[0] + direction[0],itemToExpand[1] + direction[1]) in setOfLand]
                for valid in validMoves:
                    setOfLand.remove(valid)
                    myQueue.append(valid)
                if itemToExpand in setOfLand:
                    setOfLand.remove(itemToExpand)

            counter +=1
        return counter

print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))