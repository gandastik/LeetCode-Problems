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
	c := ListNode{Val: -4}
	b := ListNode{0, &c}
	a := ListNode{2, &b}
	c.Next = &a
	head := ListNode{3, &a}
	//head.PrintList()
	detectCycle(&head).PrintList()
}

// DESC: using two pointers, faster and slower by using this two pointers technique
// we can determined that if theres a cycle on the linkedlist
// these two pointers will be on the same node at some point.
// Next we need to define where is the cycle occurs. by running
// the slow pointer and the entry pointer. these two will meet at where the cycle occurs
func detectCycle(head *ListNode) *ListNode {
	if &head == nil && &head.Next == nil {
		return nil
	}
	fast, slow, entry := head, head, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow {
			for slow != entry {
				slow = slow.Next
				entry = entry.Next
			}
			return entry
		}
	}
	return nil
}
