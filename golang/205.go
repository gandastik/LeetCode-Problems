package main

import (
	"fmt"
	//"strings"
)

func main() {
	fmt.Println(isIsomorphic("egg", "add"))
	fmt.Println(isIsomorphic("foo", "bar"))
	fmt.Println(isIsomorphic("paper", "title"))
	fmt.Println(isIsomorphic("badc", "baba"))
}

// DESC: check if characters in string s can be replaced to get string t by doing mapping dictionary
// first if the character don't have mapping, we add one in the dictionary and move on
// but if the charcter doesn't have mapping in dictionary and we add that character to be mapped with the
// existed value character then we can confirm that the two string are now Isomorphic to each other
func isIsomorphic(s string, t string) bool {
	map_s_t := map[string]string{}
	map_t_s := map[string]string{}
	for i := 0; i < len(s); i++ {
		_, ok1 := map_s_t[string(s[i])]
		_, ok2 := map_t_s[string(t[i])]
		if !ok1 && !ok2 {
			map_s_t[string(s[i])] = string(t[i])
			map_t_s[string(t[i])] = string(s[i])
		} else if map_s_t[string(s[i])] != string(t[i]) || map_t_s[string(t[i])] != string(s[i]) {
			return false
		}
	}
	return true
}
