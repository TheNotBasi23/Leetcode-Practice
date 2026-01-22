class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = -1
        rightPointer = 0
        n = len(s)
        myDict = {}
        biggestLen = 0
        while rightPointer < n:
            if s[rightPointer] in myDict:
                temp = leftPointer
                leftPointer = myDict[s[rightPointer]]
                for i in range(temp+1,myDict[s[rightPointer]] + 1):
                    myDict.pop(s[i],None)

                myDict[s[rightPointer]] = rightPointer
                rightPointer +=1
            else:
                myDict[s[rightPointer]] = rightPointer
                rightPointer +=1
            biggestLen = max(biggestLen, rightPointer - leftPointer - 1)

        return biggestLen
temp = Solution()
print(temp.lengthOfLongestSubstring(s = ""))
