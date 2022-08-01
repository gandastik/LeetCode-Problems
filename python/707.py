#707. Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

class MyLinkedList:

    def __init__(self) :
        self.head = None
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        temp = self.head
        count = 0
        while(temp):
            if(count == index):
                return temp.val
            temp = temp.next
            count+=1
        return -1

    def addAtHead(self, val: int) -> None:
        temp = self.head
        curr = MyLinkedList()
        curr.val = val
        curr.next = temp
        self.head = curr

    def addAtTail(self, val: int) -> None:
        temp = self.head
        if(temp == None):
            curr = MyLinkedList()
            curr.val = val
            self.head = curr
        while(temp):
            if(temp.next == None):
                curr = MyLinkedList()
                curr.val = val
                temp.next = curr
                break
            temp = temp.next

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        count = 0
        if(index == 0):
            self.addAtHead(val)
        while(temp):
            if(count == index-1):
                curr = MyLinkedList()
                curr.val = val
                nextNode = temp.next
                temp.next = curr
                curr.next = nextNode
                break
            count += 1
            temp = temp.next

    def deleteAtIndex(self, index: int) -> None:
        llist = self.head
        length = 0
        while(llist):
            length += 1
            llist = llist.next
        count = 0
        temp = self.head
        if(index >= length):
            return None
        #delete at the head of the linkedlist
        if(index == 0 and temp != None):
            self.head = temp.next

        while(temp):
            if(count == index - 1):
                delNode = temp.next
                temp.next = delNode.next
                break
            count += 1
            temp = temp.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)