class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        biggestCandy = 0
        for num in candies:
            biggestCandy = max(num,biggestCandy)
        return [True if num + extraCandies >= biggestCandy else False for num in candies]

