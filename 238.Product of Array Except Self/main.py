from typing import List


class Solution:
    """

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


    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp = []
        rpp = [0] * len(nums)
        n = len(nums)
        for num in nums:
            pp.append(num * (pp[-1] if pp else 1))
        for i in range(len(rpp) - 1, - 1, -1):
            rpp[i] = nums[i] * (rpp[i+1] if i+1 < n else 1)
        return [(pp[i-1] if i-1 >= 0 else 1) * (rpp[i+1] if i + 1 < n else 1) for i in range(n)]




#nums = [1,2,3,4]
#nums = [1,2,6,12]
#nums = [24,24,12,4]