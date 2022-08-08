package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "Let's take LeetCode contest"
	fmt.Println(reverseWords(s))
}

// DESC: reverse the word in the given string
func reverseWords(s string) string {
	a := strings.Split(s, " ")
	res := ""
	for i := 0; i < len(a); i++ {
		a[i] = reverseString2([]byte(a[i]))
		if i != len(a)-1 {
			res += a[i] + " "
		} else {
			res += a[i]
		}
	}
	return res
}

func reverseString2(s []byte) string {
	for i := 0; i < len(s)/2; i++ {
		s[i], s[(len(s)-1)-i] = s[(len(s)-1)-i], s[i]
	}
	return string(s)
}
