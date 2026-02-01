

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mySet = set(nums)
        for i in range(len(nums) + 1):
            if i not in mySet:
                return i
        return -1
print(Solution().missingNumber(nums = [3,0,1]))