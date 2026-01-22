from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = 1
        ps = []
        for num in nums:
            start = start * num
            ps.append(start)
        start = 1
        nums.reverse()
        reversePS = []
        for num in nums:
            start = start * num
            reversePS.append(start)
        reversePS.reverse()
        nums.reverse()
        n = len(nums)
        return [((ps[i - 1]) if 0 <i < n else 1) * ((reversePS[i + 1]) if 0 <= i < n - 1 else 1) for i in range(len(nums))]


#nums = [1,2,3,4]
#nums = [1,2,6,12]
#nums = [24,24,12,4]