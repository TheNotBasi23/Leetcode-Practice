import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        index = bisect.bisect_left(nums,target)
        print(index)
        if nums[index] == target if 0 <= index < len(nums) else False:
            secondIndex = bisect.bisect_right(nums,target)
            return [index,secondIndex - 1]
        else:
            return [-1,-1]