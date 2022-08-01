#700. You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if(root and val < root.val):
        return searchBST(root.left, val)
    elif(root and val > root.val):
        return searchBST(root.right, val)
    return root

#testcase : root = [4,2,7,1,3]
a = TreeNode(4, TreeNode(2), TreeNode(7))
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)

print(searchBST(a, 2))