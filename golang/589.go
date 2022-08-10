package main

import (
	"fmt"
)

type Node struct {
	Val      int
	Children []*Node
}

func main() {
	e := Node{Val: 6}
	d := Node{Val: 5}
	c := Node{Val: 4}
	b := Node{Val: 2}
	a := Node{3, []*Node{&d, &e}}
	head := Node{1, []*Node{&a, &b, &c}}
	fmt.Println(preorder(&head))
}

// DESC: Preorder traversal over the n-ary tree
// Using Stack and do the Depth First Search
func preorder(root *Node) []int {
	res := []int{}
	if root == nil {
		return res
	}
	stack := []*Node{}
	stack = append(stack, root)
	for len(stack) != 0 {
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, curr.Val)
		for i := len(curr.Children) - 1; i >= 0; i-- {
			stack = append(stack, curr.Children[i])
		}
	}
	return res
}
