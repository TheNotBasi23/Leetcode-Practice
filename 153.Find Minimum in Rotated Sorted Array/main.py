class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftPointer = 0
        n = len(nums)
        rightPointer = n -1
        tempSmallest = nums[0]


        while leftPointer < rightPointer:
            mid = leftPointer + (rightPointer - leftPointer) // 2
            value = nums[mid]
            if nums[mid - 1] > value and nums[(mid + 1)%n] > value:
                return value
            if tempSmallest <= value:
                leftPointer = mid + 1
            else:
                rightPointer = mid - 1

        return min(tempSmallest,nums[leftPointer])

temp = Solution()
print(temp.findMin([3,4,5,1,2]))