class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkWindowValidity(s1Contents, window):
            for key in s1Contents:
                if s1Contents[key] != window.get(key,0):
                    return False
            return True


        sizeOfWindow = len(s1)

        n = len(s2)
        if n < sizeOfWindow:
            return False
        s1Contents = {}
        for char in s1:
            s1Contents[char] = s1Contents.get(char,0) + 1
        windowContents = {}
        for i in range(sizeOfWindow):
            windowContents[s2[i]] = windowContents.get(s2[i], 0) + 1


        leftPointer = 0
        rightPointer = sizeOfWindow - 1
        for i in range(n - sizeOfWindow):
            if checkWindowValidity(s1Contents,windowContents):
                return True
            else:
                rightPointer +=1
                windowContents[s2[rightPointer]] = windowContents.get(s2[rightPointer],0) + 1
                if windowContents[s2[leftPointer]] == 1:
                    windowContents.pop(s2[leftPointer])
                else:
                    windowContents[s2[leftPointer]] -= 1
                leftPointer += 1
        if checkWindowValidity(s1Contents,windowContents):
            return True
        else:
            return False
temp = Solution()
print(temp.checkInclusion(s1 = "adc", s2 = "dcda"))


