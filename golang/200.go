package main

import (
	"fmt"
)

func main() {
	fmt.Println(numIslands([][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '1', '0'},
		{'0', '0', '0', '0', '0'},
		{'0', '0', '0', '1', '1'},
	}))
}

// DESC: find the number of islands of the given arrays contains '1' or '0'
// '1' refers to land '0' refers to water, island must consist of '1' and surrounded by '0'
// using the depth first search to find all the adjacent land and mark them
func numIslands(grid [][]byte) int {
	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == '1' {
				dfs(grid, i, j)
				count += 1
			}
		}
	}
	return count
}

func dfs(grid [][]byte, i int, j int) {
	if i < 0 || j < 0 || i >= len(grid) || j >= len(grid[i]) || grid[i][j] != '1' {
		return
	}
	grid[i][j] = '#'
	dfs(grid, i+1, j)
	dfs(grid, i-1, j)
	dfs(grid, i, j+1)
	dfs(grid, i, j-1)
}
