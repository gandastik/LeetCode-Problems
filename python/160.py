#160. Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if(headA == None or headB == None):
        return None
    llistA = headA
    llistB = headB
    while(llistA != llistB):
        llistA = headB if (llistA == None) else llistA.next
        llistB = headA if (llistB == None) else llistB.next
    return llistA

if __name__ == "__main__":
    ''''
    testcase : 
         4 -> 1 ↘
                  8 -> 4 -> 5
    5 -> 6 -> 1 ↗
    '''

    #first linkedlist
    headA = ListNode(4)
    a = ListNode(1)
    headA.next = a

    #the beginning of the intersection
    intersect = ListNode(8)
    b = ListNode(4)
    c = ListNode(5)
    intersect.next = b
    b.next = c

    #second linkedlist
    headB = ListNode(5)
    d = ListNode(6)
    e = ListNode(1)
    headB.next= d
    d.next = e
    
    #initiate the intersection
    a.next = intersect
    e.next = intersect

    #the function should return Node "intersection" which val = 8
    print(getIntersectionNode(headA, headB).val)