package main

import (
	"fmt"
)

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 2))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 7))
}

func searchInsert(nums []int, target int) int {
	return biSearch(nums, target, 0, len(nums)-1)
}

func biSearch(nums []int, target int, left int, right int) int {
	mid := (left + right) / 2
	if nums[0] > target {
		return 0
	}
	if left > right {
		return mid + 1
	}
	if nums[mid] == target {
		return mid
	} else if nums[mid] > target {
		return biSearch(nums, target, left, mid-1)
	} else if nums[mid] < target {
		return biSearch(nums, target, mid+1, right)
	}
	return mid + 1
}
