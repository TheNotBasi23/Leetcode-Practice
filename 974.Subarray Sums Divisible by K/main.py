class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps = [0]
        for num in nums:
            ps.append((num + ps[-1]) % k)
        freq = [0] * k
        freq[0] = 1
        count = 0
        for i in range(1,len(ps)):
            count += freq[ps[i]]
            freq[ps[i]] += 1


        return count