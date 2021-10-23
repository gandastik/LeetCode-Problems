#94. Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root, lst):
    if(root is not None):
        inorderTraversal(root.left, lst)
        lst.append(root.val)
        inorderTraversal(root.right, lst)
    return lst

#testcase: root = [1, null, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# # testcase : root = [1, 2]
# root = TreeNode(1)
# root.left = TreeNode(2)

lst = inorderTraversal(root, [])
print(lst)