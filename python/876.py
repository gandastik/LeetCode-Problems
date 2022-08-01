#876. Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.head = None
        self.next = None

    def printList(self):
        temp = self.head
        while(temp):
            print("{} ".format(temp.val), end="")
            temp = temp.next

    def middleNode(self):
        temp = self.head
        lst = []
        while(temp):
            lst.append(temp)
            temp = temp.next
        return lst[len(lst)//2]

if __name__ == "__main__" :
    #find the middle node of given linkedlist : 1->2->3->4->5
    llist = ListNode(1)
    llist.head = llist
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    
    llist.next = a
    a.next = b
    b.next = c
    c.next = d

    llist.printList()
    #find the middle node of the linkedlist ex. return node 'b' or (3)
    print("\n{}".format(llist.middleNode().val))