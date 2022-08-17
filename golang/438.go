package main

import (
	"fmt"
)

func main() {
	fmt.Println(findAnagrams("cbaebabacd", "abc"))
	fmt.Println(findAnagrams("abab", "ab"))
}

// DESC: given string s return an array of all the start indices of p's anagram
// TODO: need to consider this case s = "abacbabc" p = "abc"
func findAnagrams(s string, p string) []int {
  res := []int{}
  m := make(map[string]int)
  for i:=0;i<len(p);i++ {
    m[string(p[i])] += 1
  }
  //fmt.Println(m)
  copy_m := make(map[string]int)
  for key, value := range m {
    copy_m[key] = value
  }
  for i:=0;i<len(s); {
    if _, prs := m[string(s[i])]; !prs {
      i++
    for key, value := range m {
      copy_m[key] = value
    }
      continue
    } else {
      //fmt.Println(string(s[i]))
      copy_m[string(s[i])] -= 1
      if(copy_m[string(s[i])] < 0) {
        for key, value := range m {
          copy_m[key] = value
        }
        continue
      }
    }
    if findSumOfValue(copy_m) == 0 {
      res = append(res, i-len(p)+1)
      for key, value := range m {
        copy_m[key] = value
      }
      continue
    }
    i++
  }
  fmt.Println(m, copy_m)
  return res
}

func findSumOfValue(m map[string]int) int {
  sum := 0
  for _, value := range m {
    sum += value
  }
  return sum
}
