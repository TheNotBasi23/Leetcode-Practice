# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:



    def guessNumber(self, n: int) -> int:
        leftBound = 1
        rightBound = n
        def guess(n : int) -> int:
            return
        while True:
            mid = leftBound + (rightBound - leftBound) // 2
            answer = guess(mid)
            if answer == 0:
                return mid
            elif answer == -1:
                rightBound = mid - 1
            else:
                leftBound = mid + 1
