# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        finalArr = []
        q = deque()
        q.append(root)
        numToProcess = 1
        finalArr.append(root.val)
        count = 0
        while q:
            item = q.popleft()
            count +=1
            if item.left is not None:
                q.append(item.left)
            if item.right is not None:
                q.append(item.right)
            if count == numToProcess:
                if len(q) != 0:
                    numToProcess = len(q)
                    count = 0

                    finalArr.append(q[-1].val)
                else:
                    break
        return finalArr
