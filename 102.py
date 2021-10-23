#102. Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if(root is None):
        return []
    q, ret = [root], []
    while(len(q) != 0):
        size, curr = len(q), []
        for i in range(size): 
            n = q.pop(0)
            if(n.left):
                q.append(n.left)
            if(n.right):
                q.append(n.right)
            curr.append(n.val)
        ret.append(curr)
    return ret

#testcase : root = [3,9,20,null,15,7]
a = TreeNode(3, TreeNode(9), TreeNode(20))
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

print(levelOrder(a))