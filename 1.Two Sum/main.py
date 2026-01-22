class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i,num in enumerate(nums):
            if (target - num) in myDict:
                return [myDict[target-num],i]
            myDict[num] = i

temp = Solution()
print(temp.twoSum(nums = [2,7,11,15], target = 9))
