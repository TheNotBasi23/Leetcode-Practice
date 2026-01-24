class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cleanedArr = []
        for char in nums:
            if char == 0:
                cleanedArr.append(-1)
            else:
                cleanedArr.append(char)
        ps = [0]
        myDict = {0:0}
        maxLenght = -1
        for element in cleanedArr:
            value = (ps[-1] if ps else 0) + element
            ps.append(value)
            n = len(ps)
            if value not in myDict:
                myDict[value] = n - 1
            else:
                maxLenght = max(maxLenght,n - myDict[value] - 1)
        return maxLenght
print(Solution().findMaxLength(nums = [0,1,0]))
