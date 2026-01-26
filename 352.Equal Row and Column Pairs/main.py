class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        myDict = {}
        arr = []
        counter = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                arr.append(grid[j][i])

            myTuple = tuple(arr)
            myDict[myTuple] = myDict.get(myTuple,0) + 1
            arr = []
        print(myDict)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                arr.append(grid[i][j])
            myTuple = tuple(arr)
            arr = []
            if myTuple in myDict:
                counter += myDict[myTuple]
        return counter
print(Solution().equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))



