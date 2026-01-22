class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        leftPointer = 0
        rightPointer = n - 1
        maxArea = -1

        while leftPointer < rightPointer:
            width = rightPointer - leftPointer
            totalHeight = min(height[leftPointer],height[rightPointer])
            area = width * totalHeight
            maxArea = max(area,maxArea)

            if height[leftPointer] == height[rightPointer]:
                leftPointer +=1
                rightPointer -=1
            elif height[leftPointer] < height[rightPointer]:
                leftPointer +=1
            else:
                rightPointer -=1
        return maxArea

print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))