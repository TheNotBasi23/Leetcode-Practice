# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findLeftMostComp(root:TreeNode):
            if root.left is None:
                return root
            else:
                return findLeftMostComp(root.left)


        def findNode(parent,root,key):
            if root is None:
                return True
            else:
                if root.val == key:
                    if root.left is not None and root.right is not None:
                        if parent is None:
                            newParent = root.right
                            leftMostRight = findLeftMostComp(newParent)
                            leftMostRight.left = root.left
                            return False



                        else:
                            if parent.left is not None and parent.left is root:

                                parent.left = root.right
                                leftMostRight = findLeftMostComp(parent.left)
                                leftMostRight.left = root.left
                                root.left = None
                                root.right = None
                            else:
                                parent.right = root.right
                                leftMostRight = findLeftMostComp(parent.right)
                                leftMostRight.left = root.left
                                root.left = None
                                root.right = None
                    else:
                        attachment = None
                        if root.left is not None:
                            attachment = root.left
                        else:
                            attachment = root.right
                        if parent is not None:
                            if parent.left is root:
                                parent.left = attachment
                            else:
                                parent.right = attachment

                        else:
                            return False


                else:
                    if key < root.val:
                        return findNode(root,root.left,key)
                    else:
                        return findNode(root,root.right,key)


                return True
        extraEff = findNode(None,root,key)

        if extraEff is False:
            if root.left is not None and root.right is not None:
                return root.right
            else:
                if root.left is not None:
                    return root.left
                else:
                    return root.right
        else:
            return root

