class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myDict = {}
        for num in arr:
            myDict[num] = myDict.get(num, 0) + 1
        occourencesDict = {}
        for key in myDict:
            if myDict[key] in occourencesDict:
                return False
            else:
                occourencesDict[myDict[key]] = True
        return True
print(Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))
