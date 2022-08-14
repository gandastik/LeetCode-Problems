package main

import (
	"fmt"
)

func main() {
	fmt.Println(fib(2))
	fmt.Println(fib(3))
	fmt.Println(fib(6))
}

// DESC: find fibbonacci sequence F(0) = 0, F(1) = 1
// F(n) = F(n+1) + F(n+2)
func fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}
