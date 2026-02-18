from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                if stack[-1] == num:
                    newNum = num
                    while stack and stack[-1] == newNum:
                        topNum = stack.pop()
                        newNum = newNum + topNum
                    stack.append(newNum)

                else:
                    stack.append(num)
        return (stack)
Solution().mergeAdjacent([2,1,1,2])