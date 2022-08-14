package main

import (
	"fmt"
)

func main() {
	fmt.Println(climbStairs(2))
	fmt.Println(climbStairs(3))
}

// DESC: you are climbing the staircase. it takes n steps to reach the top
// you can either climb 1 or 2 steps. how many distinct ways can you climb to the top
func climbStairs(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	oneStepBefore := 2
	twoStepBefore := 1
	allWay := 0
	for i := 2; i < n; i++ {
		allWay = oneStepBefore + twoStepBefore
		twoStepBefore = oneStepBefore
		oneStepBefore = allWay
	}
	return allWay
}
