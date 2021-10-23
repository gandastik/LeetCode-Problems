#144. Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root, lst):
    if(root is not None):
        lst.append(root.val)
        preorderTraversal(root.left, lst)
        preorderTraversal(root.right, lst)
    return lst

#testcase : root = [1,null,2,3]
a = TreeNode(1, right=TreeNode(2))
a.right.left = TreeNode(3)

print(preorderTraversal(a, []))