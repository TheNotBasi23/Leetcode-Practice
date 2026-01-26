class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ps = []
        rps = [0] * n
        for num in nums:
            if not ps:
                ps.append(num)
            else:
                ps.append(ps[-1] + num)
        rightPointer = n -1
        for i in range(n-1,-1,-1):
            if i == n-1:
                rps[i] = nums[i]
            else:
                rps[i] = nums[i] + rps[i+1]
        for i in range(len(ps)):
            if (ps[i-1] if i-1 >=0 else 0) == (rps[i+1] if i+1 < n else 0) :
                return i
        return -1
        print(ps)
        print(rps)
print(Solution().pivotIndex( nums = [2,1,-1]))

