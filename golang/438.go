package main

import (
	"fmt"
)

func main() {
	fmt.Println(findAnagrams("cbaebabacd", "abc"))
	fmt.Println(findAnagrams("abab", "ab"))
}

// DESC: given string s return an array of all the start indices of p's anagram
func findAnagrams(s string, p string) []int {
  res := []int{}
  if(len(p) > len(s)) {
    return res
  }

  m := map[string]int{}
  for _, value := range p {
      m[string(value)] += 1
  }

  counter := len(m)
  begin, end := 0, 0
  //length := 1 << 30
  for (end < len(s)) {
    c := string(s[end])
    if _, prs := m[c]; prs {
      m[c] -= 1
      if(m[c] == 0) {
        counter--
      }
    }
    end++
    for counter == 0 {
      tempc := string(s[begin])
      if _, prs := m[tempc]; prs {
        m[tempc] += 1
        if(m[tempc] > 0) {
          counter++
        }
      }
      if end-begin == len(p) {
        res = append(res, begin)
      }
      begin++
    }
  }

  return res
}

//func findSumOfValue(m map[string]int) int {
//  sum := 0
//  for _, value := range m {
//    sum += value
//  }
//  return sum
//}
