package main

import (
	"fmt"
)

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{2, 3, 4}, 6))
	fmt.Println(twoSum([]int{-1, 0}, -1))
}

// DESC: given sorted array in non-descending order find the two numbers that add up to the target
// using binarsearch to find the two numbers by checking if low or high add up to target
// then adjust low or high accordingly
func twoSum(numbers []int, target int) []int {
	low, high := 0, len(numbers)-1
	for numbers[low]+numbers[high] != target {
		if numbers[low]+numbers[high] < target {
			low++
		} else {
			high--
		}
	}
	return []int{low + 1, high + 1}
}
