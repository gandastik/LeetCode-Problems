package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))
	fmt.Println(plusOne([]int{4, 3, 2, 1}))
	fmt.Println(plusOne([]int{9}))
	fmt.Println(plusOne([]int{6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3}))
}

// TODO: tis still not passed cause I did this in a way that I take the []int
// into a string and then substitue the last char with a new one by adding 1
// which is wrong when the last char is 9 -> and we can't do it in int way because
// this shit is large number > int64
func plusOne(digits []int) []int {
	str := strings.Trim(fmt.Sprint(digits), "[]")
	lastDigit, _ := strconv.Atoi(string(str[len(str)-1]))
	lastDigit += 1
	res := []int{}
	str = strings.ReplaceAll(str, " ", "")
	//fmt.Printf("%T %s %c\n", str[len(str)-1], str, str[len(str)-1])
	str = str[:len(str)-1]
	str += strconv.Itoa(lastDigit)
	//fmt.Println(str)
	//fmt.Println(lastDigit)
	for i := 0; i < len(str); i++ {
		n, _ := strconv.Atoi(string(str[i]))
		res = append(res, n)
	}
	//fmt.Printf("%T %d", str[len(str)-1], n)
	return res
}
