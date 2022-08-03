package main

import "fmt"

func main() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
}

type Stack []byte

func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) Push(c byte) {
	*s = append(*s, c)
}

func (s *Stack) Pop() byte {
	if len(*s) == 0 {
		return '-'
	} else {
		index := len(*s) - 1
		element := (*s)[index]
		*s = (*s)[:index]
		return element
	}
}

func isValid(s string) bool {
	var stack Stack
	for i := 0; i < len(s); i++ {
		if isInOpen(s[i]) {
			stack.Push(s[i])
		} else {
			if stack.isEmpty() {
				return false
			}
			c := stack.Pop()
			if isMatch(c, s[i]) {
				continue
			} else {
				return false
			}
		}
	}
	if !stack.isEmpty() {
		return false
	}
	return true
}

func isInOpen(c byte) bool {
	s := []byte{'(', '[', '{'}
	for i := 0; i < len(s); i++ {
		if s[i] == c {
			return true
		}
	}
	return false
}

func isMatch(a byte, b byte) bool {
	if a == '(' && b == ')' {
		return true
	} else if a == '[' && b == ']' {
		return true
	} else if a == '{' && b == '}' {
		return true
	}
	return false
}
