#142. Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again 
# by continuously following the next pointer. Internally, pos is used to denote the index of the node 
# that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Notice that you should not modify the linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return None
        slow = head
        fast = head
        entry = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                while(slow != entry):
                    slow = slow.next
                    entry = entry.next
                return entry
        return None

if __name__ == "__main__":
    #ex. if cycle begin at pos 1
    head = ListNode(3)
    a = ListNode(2)
    b = ListNode(0)
    c = ListNode(-4)
    c.next = a
    a.next = b
    b.next = c
    head.next = a

    print(detectCycle(head))