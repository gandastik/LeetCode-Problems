package main

import (
	"fmt"
)

func main() {
	fmt.Println(backspaceCompare("ad#c", "ad#c"))
	fmt.Println(backspaceCompare("ab##", "c#d#"))
	fmt.Println(backspaceCompare("a#c", "b"))
}

// DESC: compare the give two string by representing the '#' as the backspace
// Soln: using stack to pop the last byte out when found '#'
func backspaceCompare(s string, t string) bool {
	stack_s := []byte{}
	stack_t := []byte{}
	for i := 0; i < len(s); i++ {
    if s[i] == '#' {
      if(len(stack_s) == 0) {
        continue
      }
      stack_s = stack_s[:len(stack_s)-1]
    } else {
      stack_s = append(stack_s, s[i])
    }
	}
	for i := 0; i < len(t); i++ {
    if t[i] == '#' {
      if(len(stack_s) == 0) {
        continue
      }
      stack_t = stack_t[:len(stack_t)-1]
    } else {
      stack_t = append(stack_t, t[i])
    }
	}
  fmt.Println("stack_s : ", stack_s)
  fmt.Println("stack_t : ", stack_t)
  return compareSlice(stack_s, stack_t)
}

func compareSlice(a []byte, b []byte) bool {
  if len(a) != len(b) {
    return false
  }
  for i := 0;i<len(a);i++ {
    if(a[i] != b[i]) {
      return false
    }
  }
  return true
}
