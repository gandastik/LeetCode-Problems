package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
}

func lengthOfLastWord(s string) int {
	s = strings.Trim(s, " ")
	res := strings.Split(s, " ")
	fmt.Println(res)
	return len(res[len(res)-1])
}
