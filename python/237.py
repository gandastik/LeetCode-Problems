#237. Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, 
# instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.

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

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    #create linkedlist of 4->5->1->9
    head = ListNode(4)
    head.head = head
    a = ListNode(5)
    b = ListNode(1)
    c = ListNode(9)
    head.next = a
    a.next = b
    b.next = c

    #delete node 5 results: 4->1->9
    head.deleteNode(a)

    head.printList()
