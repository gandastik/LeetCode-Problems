package main

import (
	"fmt"
)

func main() {
	s := []byte{'h', 'e', 'l', 'l', 'o'}
	fmt.Println("s before reverse : ", s)
	reverseString(s)
	fmt.Println("s after reverse : ", s)
}

// DESC: revser the given string. Sol: find the middle index of the given string
// the we swap the beginning of the string and the end
// and keep doing it until we reach the middle of the string
func reverseString(s []byte) {
	for i := 0; i < len(s)/2; i++ {
		s[i], s[(len(s)-1)-i] = s[(len(s)-1)-i], s[i]
	}
}
