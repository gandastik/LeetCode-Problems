package main

import (
	"fmt"
)

func main() {
	nums := []int{0, 1, 0, 3, 12}
	fmt.Println("nums before move zeroes :", nums)
	moveZeroes(nums)
	fmt.Println("nums after move zeroes :", nums)
	nums = []int{0, 0, 1}
	fmt.Println("nums before move zeroes :", nums)
	moveZeroes(nums)
	fmt.Println("nums after move zeroes :", nums)
}

// DESC: move found zero to the end of array by not interfere with the order of others
// find all non zero and move it in the front by using another index (k)
// then we know how many zero we foudn by len(nums) - k , next we need to add zero to the end of the array
// by looping len(nums)-k times and using k as index to add zero
func moveZeroes(nums []int) {
	k := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[k] = nums[i]
			k++
		}
	}
	for ; k < len(nums); k++ {
		nums[k] = 0
	}
}
