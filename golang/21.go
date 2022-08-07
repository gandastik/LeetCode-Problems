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
	b := ListNode{Val: 4}
	a := ListNode{2, &b}
	head := ListNode{1, &a}
	head.PrintList()

	d := ListNode{Val: 4}
	c := ListNode{3, &d}
	head2 := ListNode{1, &c}
	head2.PrintList()
	mergeTwoLists(&head, &head2).PrintList()
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	ptr := list1
	if list1.Val > list2.Val {
		ptr = list2
		list2 = list2.Next
	} else {
		list1 = list1.Next
	}
	curr := ptr
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}
	if list1 == nil {
		curr.Next = list2
	} else {
		curr.Next = list1
	}
	return ptr
}
