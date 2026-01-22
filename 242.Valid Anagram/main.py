class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        else:
            myDict1 = {}
            for char in s:
                myDict1[char] = myDict1.get(char,0) + 1
            for char in t:
                if char not in myDict1:
                    return False
                else:
                    if myDict1[char] == 1:
                        myDict1.pop(char,None)
                    else:
                        myDict1[char] -= 1
            return True

