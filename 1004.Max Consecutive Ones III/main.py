class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        leftPointer = rightPointer = 0
        n = len(nums)
        indicesOfZero = [i for i in range(n-1,-1,-1) if nums[i] == 0]
        maxSet = 0
        zeroInstance = 0
        while rightPointer < n:
            if nums[rightPointer] == 1:
                rightPointer += 1
            else:
                zeroInstance += 1
                if zeroInstance > k:
                    maxSet = max(maxSet,rightPointer - leftPointer )
                    leftPointer = indicesOfZero.pop() + 1
                    rightPointer += 1
                    zeroInstance -= 1
                else:
                    rightPointer += 1
        return max(rightPointer - leftPointer , maxSet)
print(Solution().longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))