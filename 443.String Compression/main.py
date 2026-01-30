class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        leftPointer = 0
        rightPointer = 0
        writingPointer = 0
        while rightPointer < n:
            while rightPointer < n and chars[rightPointer] == chars[leftPointer]:
                rightPointer +=1
            if rightPointer - leftPointer == 1:
                chars[writingPointer] = chars[leftPointer]
                leftPointer +=1
                writingPointer +=1
            else:
                chars[writingPointer] = chars[leftPointer]
                writingPointer += 1
                numAsStr = str(rightPointer - leftPointer)
                lenDist = len(numAsStr)

                for i in range(writingPointer, writingPointer + lenDist):
                    chars[i] = numAsStr[i - writingPointer]
                writingPointer += lenDist
                leftPointer = rightPointer
        chars = chars[0:writingPointer]
        return writingPointer + 1



chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(chars)
print(Solution().compress(chars))




