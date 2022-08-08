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
	head.PrintList()
	middleNode(&head).PrintList()
}

// DESC: count all the nodes and then find the middle index,
// next is just traverse the node to the index and return that node
func middleNode(head *ListNode) *ListNode {
	temp := head
	count := 0
	for ; temp.Next != nil; temp = temp.Next {
		count++
	}
	count += 1
	middle := count / 2
	res := head
	for i := 0; i < middle; i++ {
		res = res.Next
	}
	return res
}
