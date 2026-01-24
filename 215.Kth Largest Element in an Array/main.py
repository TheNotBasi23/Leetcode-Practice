import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k
        def findValue(l,r):
            randomIndex = random.randint(l,r)
            nums[randomIndex],nums[r] = nums[r], nums[randomIndex]
            leftPointer = l
            for i in range(l,r):
                print(nums)
                if nums[i] < nums[r]:
                    nums[i], nums[leftPointer] = nums[leftPointer], nums[i]
                    leftPointer +=1
            nums[r], nums[leftPointer] = nums[leftPointer], nums[r]
            if leftPointer == k:
                return nums[leftPointer]
            elif leftPointer < k :
                return findValue(leftPointer + 1, r)
            else:
                return findValue(l,leftPointer - 1)

        return findValue(0,n-1)


print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))