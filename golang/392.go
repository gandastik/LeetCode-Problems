package main

import (
	"fmt"
)

func main() {
	fmt.Println(isSubsequence("abc", "ahbgdc"))
	fmt.Println(isSubsequence("axc", "ahbgdc"))
}

func isSubsequence(s string, t string) bool {
	n, m := len(s), len(t)
	j := 0
	for i := 0; i < m && j < n; i++ {
		if s[j] == t[i] {
			j++
		}
	}
	return j == n
}
