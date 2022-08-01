#19. Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    temp = head
    while(temp):
        print("{} ".format(temp.val), end="")
        temp = temp.next

def removeNthFromEnd(head, n) -> ListNode:
    temp = head
    llist = head
    tempB = llist
    length = 0
    #find the length of the given linked list
    while(temp):
        length+=1
        temp = temp.next
    #delete the first node of the linked list
    if(length - n == 0 and tempB != None):
        llist = tempB.next
    count = 0
    #delete the nth node from the linked list
    while(tempB):
        if(count == length - n - 1):
            delNode = tempB.next
            tempB.next = delNode.next
            break
        tempB = tempB.next
        count += 1
    return llist

if __name__ == "__main__":
    '''
    testcase : head : 1 -> 2 -> 3 -> 4 -> 5 , n = 2
    result : 1 -> 2 -> 3 -> 5
    '''

    #setups
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    head.next = a
    a.next = b
    b.next = c
    c.next = d

    printList(removeNthFromEnd(head, 2))