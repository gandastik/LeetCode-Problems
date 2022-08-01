#203. Given the head of a linked list and an integer val, 
#remove all the nodes of the linked list that has Node.val == val, and return the new head.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def printList(head):
    temp = head
    while(temp):
        print("{} ".format(temp.val), end="")
        temp = temp.next

def removeElements(head: ListNode, val: int):
    ret = head
    temp = ret
    index = 0
    while(temp):
        if(temp.val == val):
            temp = removeNode(ret, index)
            ret = temp
            # printList(ret)
            index=0
            continue
        if(temp != None):
            temp = temp.next
        index+=1
    if(ret != None):
        if(ret.val == val):
            return None
    return ret


def removeNode(head: ListNode, n: int):
    ret = head
    temp = ret
    count = 0
    if(n == 0 and temp != None):
        ret = temp.next
        return ret
    while(temp):
        if(n-1 == count):
            delNode = temp.next
            temp.next = delNode.next
            break
        temp = temp.next
        count+=1
    return ret

if __name__ == "__main__":
    '''
    testcase:
    1). 1->2->6->3->4->5->6 val=6 result: 1->2->3->4->5
    2). 1->2->2->2->2 val=1 result: 2->2->2->2
    3). None val=1 result: None
    4). 7->7->7->7 val=7 result: None
    
    '''
    lst = [int(x) for x in input().split()]
    val = int(input())
    head = ListNode(lst[0])
    nodes = lst[1:]
    temp = head
    for i in nodes:
        a = ListNode(i)
        temp.next = a
        temp = temp.next

    printList(removeElements(head, val))