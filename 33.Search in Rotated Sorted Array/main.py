from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1
        while leftPointer < rightPointer:
            mid = leftPointer + (rightPointer - leftPointer) // 2
            value = nums[mid]
            if value == target:
                return mid
            else:
                if nums[leftPointer] < nums[mid]:
                    if nums[leftPointer] <= target <= nums[mid-1]:
                        rightPointer = mid - 1
                    else:
                        leftPointer = mid + 1
                else:
                    if nums[mid+1] <= target <= nums[rightPointer]:
                        leftPointer = mid + 1
                    else:
                        rightPointer = mid - 1
        if nums[leftPointer] == target:
            return leftPointer
        else:
            return -1

temp = Solution()
print(temp.search(nums = [3,1], target = 1
))


