import bisect
import math


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        arr = []
        potions.sort()
        for i in range(len(spells)):
            bound = success / spells[i]
            indexOfInsert = bisect.bisect_left(potions, bound)
            numPairs = len(potions) - indexOfInsert
            arr.append(numPairs)
        return arr

print(Solution().successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16))