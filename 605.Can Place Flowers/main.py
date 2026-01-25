class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        leftPointer = 0
        counter = 0
        while leftPointer < len(flowerbed):

            if flowerbed[leftPointer] == 0 and (flowerbed[leftPointer - 1] == 0 if leftPointer - 1 >= 0 else True) and (
            flowerbed[leftPointer + 1] == 0 if leftPointer + 1 < len(flowerbed) else True):
                counter += 1
                leftPointer += 1
            elif flowerbed[leftPointer] == 1:
                leftPointer += 1
            if counter >= n:
                return True
            leftPointer += 1

        return False