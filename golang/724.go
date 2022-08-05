package main

import (
	"fmt"
)

func main() {
	fmt.Println(pivotIndex([]int{1, 7, 3, 6, 5, 6}))
	fmt.Println(pivotIndex([]int{1, 2, 3}))
	fmt.Println(pivotIndex([]int{2, 1, -1}))
}

// O(n)
func pivotIndex(nums []int) int {
	sum, leftSum := 0, 0
	for _, num := range nums {
		sum += num
	}
	for i := 0; i < len(nums); i++ {
		if leftSum == sum-leftSum-nums[i] {
			return i
		}
		leftSum += nums[i]
	}
	return -1
}

// This solution works too but it's too slow -> O(n^2)
// func pivotIndex(nums []int) int {
// 	for i := 0; i < len(nums); i++ {
// 		leftSum := findSumOfArr(nums[:i+1]) // these is the thing that makes it slow
// 		rightSum := findSumOfArr(nums[i:])
// 		if leftSum == rightSum {
// 			return i
// 		}
// 	}
// 	return -1
// }
//
// func findSumOfArr(arr []int) int {
// 	res := 0
// 	for _, num := range arr {
// 		res += num
// 	}
// 	return res
// }
