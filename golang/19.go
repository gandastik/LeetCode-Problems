package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func (n ListNode) PrintList() {
	for ; n.Next != nil; n = *n.Next {
		fmt.Print(n.Val, "->")
	}
	fmt.Print(n.Val)
	fmt.Println()
}

func main() {
	d := ListNode{Val: 5}
	c := ListNode{4, &d}
	b := ListNode{3, &c}
	a := ListNode{2, &b}
	head := ListNode{1, &a}
	removeNthFromEnd(&head, 2).PrintList()
	a = ListNode{Val: 2}
	head = ListNode{1, &a}
	removeNthFromEnd(&head, 1).PrintList()
	head = ListNode{Val: 1}
	removeNthFromEnd(&head, 1).PrintList() // return nil
}

// DESC: remove the nth node from the end of the linkedlist.
// explaination: first find the length of the linkedlist, next traverse to the
// node before the node that we need to remove then remove the wanted node by doing
// curr.next = curr.next.next then we return the head of the linkedlist
// Time Complex: O(n) [I think...]
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	curr := head
	count := 0
	fmt.Println("length : ", findLength(head))
	length := findLength(head)
	// for the case that the wanted node are the head of the linkedlist
	if n+1 > length {
		return curr.Next
	}
	for curr != nil {
		// traverse to the node before the wanted node
		if count == length-(n+1) {
			break
		}
		curr = curr.Next
		count++
	}
	curr.Next = curr.Next.Next
	return head
}

// DESC: find the length of the given linkedlist
func findLength(head *ListNode) int {
	curr := head
	count := 0
	for curr != nil {
		curr = curr.Next
		count++
	}
	return count
}
