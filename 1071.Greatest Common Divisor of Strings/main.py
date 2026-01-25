import math
import heapq
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def generateFactors(num):
            setOfFactors = set()
            for i in range(1,math.ceil(math.sqrt(num)) + 1):
                if num % i == 0:
                    setOfFactors.add(i)
                    setOfFactors.add(num // i)
            return setOfFactors
        value = str1 + str2
        setOfFactors1 = generateFactors(len(str1))
        setOfFactors2 = generateFactors(len(str2))
        unionFactors = setOfFactors1.intersection(setOfFactors2)
        arr = []
        while unionFactors:
            arr.append(-unionFactors.pop())
        heapq.heapify(arr)

        valid = True
        while arr:
            currFactor = -heapq.heappop(arr)
            keyWord = value[0:currFactor]
            for i in range(0, len(value), currFactor):
                if not value.startswith(keyWord,i):
                    valid = False
                    break
            if valid:
                return keyWord

        return ""

print(Solution().gcdOfStrings(str1 = "AAAAAB", str2 = "AAA"))