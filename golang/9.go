package main

import "fmt"

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(10))
}

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	num := 0
	for temp := x; temp > 0; temp /= 10 {
		r := temp % 10
		num += r
		num *= 10
	}
	num = num / 10
	if num == x {
		return true
	}
	return false
}
