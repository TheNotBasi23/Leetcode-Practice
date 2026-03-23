class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myDict = {}
        for myStr in strs:
            newStr = "".join(sorted(myStr))
            if newStr in myDict:
                myDict[newStr].append(myStr)
            else:
                myDict[newStr] = [myStr]
        finalArr = []
        for key,val in myDict.items():
            finalArr.append(val)
        return (finalArr)
Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])