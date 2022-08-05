package main

import (
	"fmt"
)

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 2))
}

func search(nums []int, target int) int {
	return biSearch(nums, target, 0, len(nums)-1)
}

func biSearch(nums []int, target int, left int, right int) int {
	if left > right {
		return -1
	}
	mid := (right + left) / 2
	if nums[mid] == target {
		return mid
	} else if nums[mid] > target {
		return biSearch(nums, target, left, mid-1)
	} else if nums[mid] < target {
		return biSearch(nums, target, mid+1, right)
	}
	return -1
}
