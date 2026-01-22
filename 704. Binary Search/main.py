import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums,target)
        if 0 <= index <len(nums):
            if nums[index] == target:
                return index
            else:
                return -1
        else:
            return -1

temp = Solution()
print(temp.search(nums = [-1,0,3,5,9,12], target = 2))

