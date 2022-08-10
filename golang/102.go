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
	d := TreeNode{Val: 7}
	c := TreeNode{Val: 15}
	b := TreeNode{Val: 20, Left: &c, Right: &d}
	a := TreeNode{Val: 9}
	head := TreeNode{Val: 3, Left: &a, Right: &b}

	fmt.Println(levelOrder(&head))
}

// DESC: Binary Tree Level Order Traversal
// Implementing the Breadth First Search using Queue
func levelOrder(root *TreeNode) [][]int {
	q := []*TreeNode{}
	res := [][]int{}
	if root == nil {
		return res
	}
	q = append(q, root)
	for len(q) != 0 {
		n := len(q)
		list := []int{}
		for i := 0; i < n; i++ {
			curr := q[0]
			if curr.Left != nil {
				//Enqueue
				q = append(q, curr.Left)
			}
			if curr.Right != nil {
				//Enqueue
				q = append(q, curr.Right)
			}
			//Dequeue
			list = append(list, curr.Val)
			q = q[1:]
		}
		res = append(res, list)
	}
	return res
}
