class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minLen = min(len(char) for char in strs)

        pointer = 0
        finish = False
        final = []
        while pointer < minLen:
            curr = strs[0][pointer]
            for element in strs:
                if element[pointer] != curr:
                    finish = True
                    break
            if finish:
                break
            else:
                final.append(curr)
                pointer += 1
        return ("".join(final))
Solution().longestCommonPrefix(strs = ["dog","racecar","car"])