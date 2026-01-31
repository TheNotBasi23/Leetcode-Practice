class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        leftPointer = 0
        rightPointer = n - 1
        while leftPointer< rightPointer:
            mid = leftPointer + (rightPointer -leftPointer) // 2
            if nums[mid] < nums[mid + 1]:
                leftPointer = mid + 1
            elif nums[mid-1] > nums[mid]:
                rightPointer = mid - 1
            elif nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid-1] < nums[mid]:
                return mid
        return leftPointer


    def findPeakElementSecondSolution(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l





print(Solution().findPeakElement(nums = [1,2,1,3,5,6,4]))