from sys import prefix


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        myDict = {}
        counter = 0
        for element in nums:
            if (k-element) in myDict:
                counter +=1
                if myDict[(k-element)] == 1:
                    myDict.pop((k-element), None)
                else:
                    myDict[(k - element)] -= 1
            else:
                myDict[element] = myDict.get(element,0) + 1
        return (counter)

