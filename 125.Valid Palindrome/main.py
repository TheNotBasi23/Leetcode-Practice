class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [char.lower() for char in s if char.isalpha() or char.isnumeric()]
        temp = [arr[i] for i in range(len(arr) - 1, -1, -1)]
        for key,value in zip(arr,temp):
            if key != value:
                return False
        return True
temp = Solution()
print(temp.isPalindrome(s = "0P"))

