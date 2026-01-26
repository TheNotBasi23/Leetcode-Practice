class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ps = [0]
        highestPoint  = 0
        for num in gain:
            ps.append(num + ps[-1])
            highestPoint = max(highestPoint,ps[-1])
        return highestPoint
