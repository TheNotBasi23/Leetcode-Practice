class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1
        while leftPointer < rightPointer:
            mid = leftPointer + (rightPointer - leftPointer) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                leftPointer = mid + 1
            else:
                rightPointer = mid - 1
        if nums[leftPointer] == target:
            return leftPointer
        else:
            return -1



temp = Solution()
print(temp.search(nums = [-1,0,3,5,9,12], target = 0))

