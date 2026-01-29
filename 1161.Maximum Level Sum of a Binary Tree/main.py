# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        currSum = 0
        maxSum = root.val if root is not None else 0
        biggestSumLevel = 1
        currLevel = 1
        count = 0
        itemsToProcess = len(q)
        while q:
            item = q.popleft()
            if item.left is not None:
                q.append(item.left)
            if item.right is not None:
                q.append(item.right)
            count += 1
            currSum += item.val
            if count == itemsToProcess:
                if currSum > maxSum:
                    biggestSumLevel = currLevel

                    maxSum = currSum
                currSum = 0
                currLevel += 1
                itemsToProcess = len(q)
                count = 0
        return biggestSumLevel

