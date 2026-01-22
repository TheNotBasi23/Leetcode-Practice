class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        visitedIValues = {}
        for i in range(n - 2):
            if nums[i] in visitedIValues:
                continue
            else:
                visitedIValues[nums[i]] = True
            boundedValue = nums[i]
            leftPointer = i + 1
            rightPointer = n - 1
            newTarget = -boundedValue
            while leftPointer < rightPointer:
                temp = nums[leftPointer] + nums[rightPointer]
                if temp == newTarget:
                    ans.append([nums[i],nums[leftPointer],nums[rightPointer]])

                    value = nums[leftPointer]
                    while value == nums[leftPointer]:
                        leftPointer +=1
                    value = nums[rightPointer]
                    while value == nums[rightPointer]:
                        rightPointer -= 1

                    #may cause some issues
                elif temp > newTarget:
                    rightPointer -= 1
                else:
                    leftPointer +=1
        return ans

print(Solution().threeSum([-1,0,1,2,-1,-4]))

