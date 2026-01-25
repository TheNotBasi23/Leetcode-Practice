from typing import final


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        stack = []
        for element in s:
            if not stack:
                stack.append(element)
            else:
                if not (element == " " and stack[-1] == " "):
                    stack.append(element)

        cleanedStr = "".join(stack)
        cleanedArr = cleanedStr.split(" ")
        cleanedArr.reverse()
        n = len(cleanedArr)
        newArr = []
        for i in range(n):
            if i != n - 1:
                newArr.append(cleanedArr[i])
                newArr.append(" ")
            else:
                newArr.append(cleanedArr[i])
        final = "".join(newArr)

        return final

Solution().reverseWords(s = "the sky is blue")