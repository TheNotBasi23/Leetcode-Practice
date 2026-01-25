class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a":True,"e":True,"i":True,"o":True,"u":True,"A":True,"E":True,"I":True,"O":True,"U":True}
        stack = [char for char in s if char in vowels]
        arr = []
        for element in s:
            if element in vowels:
                arr.append(stack.pop(-1))
            else:
                arr.append(element)
        return "".join(arr)


print(Solution().reverseVowels(s = "IceCreAm"))