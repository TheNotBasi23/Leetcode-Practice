import math
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcEuc(x,y):
            val1 = x * x
            val2 = y * y
            combo =  val1 + val2
            return combo
        arr = [( calcEuc(i,j),(i,j)) for i,j in points]
        print(arr)
        k = len(arr) - k
        maxLen = len(arr)
        def quickSearch(l,r):
            leftPoiunter = l
            randomIndex = random.randint(l,r)
            arr[randomIndex],arr[r] = arr[r], arr[randomIndex]
            for i in range(l,r):
                if arr[i][0] > arr[r][0]:
                    arr[i], arr[leftPoiunter] = arr[leftPoiunter], arr[i]
                    leftPoiunter +=1
            arr[leftPoiunter], arr[r] = arr[r], arr[leftPoiunter]
            print(arr)

            if leftPoiunter == k:
                return [[arr[i][1][0],arr[i][1][1]] for i in range(leftPoiunter,maxLen)]
            elif leftPoiunter < k:
                return quickSearch(leftPoiunter + 1, r)
            else:
                return quickSearch(l,leftPoiunter - 1)

        return quickSearch(0,len(arr) - 1)

print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))
