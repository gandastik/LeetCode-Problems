#450. Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, val):
    if(root is None):
        return None
    if(val < root.val):
        root.left = deleteNode(root.left, val)
    elif(val > root.val):
        root.right = deleteNode(root.right, val)
    else:
        if(root.left is None):
            return root.right
        elif(root.right is None):
            return root.left
        else:
            smallestNode = root.right
            while(smallestNode.left):
                smallestNode = smallestNode.left
            smallestNode.left = root.left
            return root.right
    return root

#testcase : root = [5,3,6,2,4,null,7], val = 3
root = TreeNode(5, TreeNode(3), TreeNode(6))
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

ret = deleteNode(root, 3)
print(ret.val)