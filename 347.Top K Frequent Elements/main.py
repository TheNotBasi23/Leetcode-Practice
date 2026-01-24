import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for num in nums:
            myDict[num] = myDict.get(num,0) + 1

        arr = [(key,myDict[key]) for key in myDict]
        k = len(arr) - k

        l = 0
        r = len(arr) - 1
        maxLen = len(arr)
        def quickSelect(l,r):
            randomIndex = random.randint(l,r)
            arr[randomIndex],arr[r] = arr[r],arr[randomIndex]
            leftPointer = l
            for i in range(l,r):
                if arr[i][1] < arr[r][1]:
                    arr[i], arr[leftPointer] = arr[leftPointer],arr[i]
                    leftPointer +=1
            arr[leftPointer] , arr[r] = arr[r] , arr[leftPointer]
            if leftPointer == k:
                return [arr[i][0] for i in range(k,maxLen)]
            elif leftPointer < k:
                return quickSelect(leftPointer + 1, r)
            else:
                return quickSelect(l, leftPointer - 1)


        return quickSelect(l,r)

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
