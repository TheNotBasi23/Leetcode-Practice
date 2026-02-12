class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        containers = [[] for _ in range(numRows)]
        down = True
        counter = 0
        level = 0
        n = len(s)
        print(containers)
        while counter < n:
            containers[level].append(s[counter])
            if down:
                level+=1
                if level == numRows - 1:
                    down = False
            else:
                level -= 1
                if level == 0:
                    down = True
            counter += 1
        stringArr = ["".join(char) for char in containers]
        finalStr = "".join(stringArr)
        return finalStr
print(
Solution().convert(s = "PAYPALISHIRING", numRows = 3)

)
