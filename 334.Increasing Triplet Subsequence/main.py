class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestNum = float('inf')
        secondSmallestNum = float('inf')
        for num in nums:
            if num <= smallestNum:
                smallestNum = num
            elif num <= secondSmallestNum:
                secondSmallestNum = num
            else:
                return True
        return False