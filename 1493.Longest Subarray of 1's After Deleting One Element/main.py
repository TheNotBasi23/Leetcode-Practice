class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append([num,1])
            else:
                if stack[-1][0] == num:
                    stack[-1][1] +=1
                else:
                    stack.append([num,1])
        if len(stack) == 1:
            if stack[0][0] == 1:
                return stack[0][1] - 1
            else:
                return 0


        ones = [(i,arr) for i, arr in enumerate(stack) if arr[0] == 1 ]
        maxLen = -1
        n = len(stack)
        for i, arr in ones:
            maxLen = max(maxLen,arr[1])
            if (stack[i+1][1] == 1 if i+1 < n else False):
                maxLen = max(maxLen, arr[1] + (stack[i+2][1] if i+2 < n else 0))
            if (stack[i-1][1] == 1 if i-1 >= 0 else False):
                maxLen = max(maxLen, arr[1] + (stack[i-2][1] if i-2 >= 0 else 0))
        return (maxLen)
Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1])