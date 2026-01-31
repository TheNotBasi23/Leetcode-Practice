import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def genAnswer(k,piles,h):
            count = 0
            for num in piles:
                value = math.ceil(num // k)
                count += value if num % k == 0 else value + 1
            if count > h:
                return False
            else:
                return True

        leftPointer,rightPointer = 1, max(piles)
        while leftPointer < rightPointer:
            mid = leftPointer + (rightPointer - leftPointer) // 2
            print(mid)
            if genAnswer(mid,piles,h):
                rightPointer = mid
            else:
                leftPointer = mid + 1
        return leftPointer
print(Solution().minEatingSpeed(piles = [2,2], h = 4))
