#173. Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorderLst = []
        self.count = -1
        
        curr = self.root
        s = []
        while(True):
            if(curr is not None):
                s.append(curr)
                curr = curr.left
            elif(len(s) != 0):
                curr = s.pop()    
                self.inorderLst.append(curr.val)
                curr = curr.right
            else:
                break    

    def next(self) -> int:
        self.count += 1
        return self.inorderLst[self.count]
        

    def hasNext(self) -> bool:
        return self.count < len(self.inorderLst)-1