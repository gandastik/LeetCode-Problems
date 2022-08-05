package main

import (
	"fmt"
)

func main() {
	fmt.Println(firstBadVersion(5))
	fmt.Println(firstBadVersion(1))
}

// DESCRIPT: this is done in the site but can not do it locally because
// you need a pre-defined function
func firstBadVersion(n int) int {
	return n
}
