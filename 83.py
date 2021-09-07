#83. Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self, head = None):
        if(head == None):
            self.head = None
        else:
            head = head

    def append(self, val):
        node = Node(val)
        if(self.head == None):
            self.head = node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node
    
    def __str__(self):
        s = ''
        temp = self.head
        while(temp):
            s += str(temp.val) + ' '
            temp = temp.next
        return s

def deleteDuplicates(head):
    cur = head
    while(cur):
        while(cur.next and cur.val == cur.next.val):
            cur.next = cur.next.next
        cur = cur.next
    return head

if __name__ == "__main__":
    lst = [int(x) for x in input().split()]
    head = List()
    for i in lst:
        n = Node(i)
        head.append(n.val)
    deleteDuplicates(head.head)
    print(f'after deleted duplicates : {head}')