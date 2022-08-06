package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(sortedSquares([]int{-4, -1, 0, 3, 10}))
	fmt.Println(sortedSquares([]int{-7, -3, 2, 3, 11}))
}

func sortedSquares(nums []int) []int {
	for idx, num := range nums {
		nums[idx] = num * num
	}
	sort.Ints(nums)
	return nums
}
