package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	b := TreeNode{Val: 3}
	a := TreeNode{Val: 1}
	head := TreeNode{2, &a, &b}
	fmt.Println(isValidBST(&head))
	d := TreeNode{Val: 6}
	c := TreeNode{Val: 3}
	b = TreeNode{4, &c, &d}
	a = TreeNode{Val: 1}
	head = TreeNode{Val: 5, Left: &a, Right: &b}
	fmt.Println(isValidBST(&head))
}

// DESC: validate the binary search tree
// using the iterative methods by check if the previous node is less than the parent node
func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	stack := []*TreeNode{}
	var pre *TreeNode
	for root != nil || len(stack) != 0 {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pre != nil && root.Val <= pre.Val {
			return false
		}
		pre = root
		root = root.Right
	}
	return true
}
