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
	b := ListNode{Val: 3}
	a := ListNode{2, &b}
	head := ListNode{1, &a}
	head.PrintList()
	reverseList(&head).PrintList()
}

// DESC: reverse the linkedlist
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head
	for curr != nil {
		nextNode := curr.Next
		curr.Next = prev
		prev = curr
		curr = nextNode
	}
	return prev
}
