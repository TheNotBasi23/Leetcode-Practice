class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ps = []
        for num in nums:
            if not ps:
                ps.append(num)
            else:
                ps.append(num + ps[-1])
        biggestAvg = -999999
        for i in range(k - 1,len(ps)):
            totalSum = ps[i] - (ps[i - k] if i -k  >=0 else 0)
            print(totalSum)
            totalAverage = totalSum / k
            biggestAvg = max(totalAverage,biggestAvg)
        return round(biggestAvg,5)
print(Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))

