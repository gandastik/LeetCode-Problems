#100. Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def isSameTree(p, q):
    if(p and q):
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return q is p

#testcase : p = [1,2,3], q = [1,2,3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
# #testcase : p = [1,2,1] q = [1,1,2]
# p = TreeNode(1, TreeNode(2), TreeNode(1))
# q = TreeNode(1, TreeNode(1), TreeNode(2))

print(isSameTree(p, q))