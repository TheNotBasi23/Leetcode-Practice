class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        for i, num in enumerate(nums):
            if num in myDict:
                value = abs(myDict[num] - i)
                if value <= k:
                    return True
                else:
                    myDict[num] = i
            else:
                myDict[num] = i

        return False
temp = Solution()
print(temp.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2
))