#Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.head = None
        self.next = None

    def printList(self):
        temp = self.head
        while(temp):
            print("{} ".format(temp.val), end="")
            temp = temp.next

    def decimalValue(self) -> int:
        num = 0
        temp = self.head
        while(temp):
            num = num << 1 | temp.val
            temp = temp.next
        return num

if __name__ == "__main__":
    #example of the given linkedlist is : 1->0->1->1 = 11 in decimal
    llist = ListNode(1)
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(1)
    llist.head = llist
    llist.next = a
    a.next = b
    b.next = c

    llist.printList()
    #find the decimal value of the binary linkedlist
    print("\ndecimal value of the linkedlist is : {}".format(llist.decimalValue()))