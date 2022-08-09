package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(maxProfit([]int{7, 6, 4, 3, 1}))
}

// DESC: find the max profit by choosing a single day to buy a stock and
// choosing a different day in the future to sell that stock
func maxProfit(prices []int) int {
	max := float64(0)
	min := float64(1 << 62)
	for _, price := range prices {
		min = math.Min(float64(price), min)
		max = math.Max(float64(price)-min, max)
	}
	return int(max)
}
