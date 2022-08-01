#701. You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    newNode = TreeNode(val)
    if(root is None):
        root = newNode
        return root
    if(val < root.val):
        if(root.left):
            insertIntoBST(root.left, val)
        else:
            root.left = newNode
    if(val > root.val):
        if(root.right):
            insertIntoBST(root.right, val)
        else:
            root.right = newNode
    return root

#testcase : root = [4,2,7,1,3], val = 5
#output :
    #     4
    #    / \
    #   2   7
    #  / \ /
    # 1  3 5
a = TreeNode(4, TreeNode(2), TreeNode(7))
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)

print(insertIntoBST(a, 5))