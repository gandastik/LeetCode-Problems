package main

import (
	"fmt"
)

func main() {
	fmt.Println(removeElement([]int{3, 2, 2, 3}, 3))
	fmt.Println(removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2))
}

func removeElement(nums []int, val int) int {
	i := 0
	for idx, num := range nums {
		if num != val {
			nums[i] = nums[idx]
			i++
		}
	}
	fmt.Println(nums, val)
	return i
}
