package main

import (
	"fmt"
)

func main() {
	fmt.Println(floodFill([][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}, 1, 1, 2))
}

// DESC: floodfill the cell with the newcolor by chaning the 4-directionally connected to the starting pixel and to those pixels and so on
// using depth first search recursive methods to keep flooding the color to the adjacendy cell
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	oldColor := image[sr][sc]
	if oldColor != color {
		dfs(image, sr, sc, oldColor, color)
	}
	return image
}

func dfs(image [][]int, r int, c int, color int, newColor int) {
	if image[r][c] == color {
		image[r][c] = newColor
		if r >= 1 {
			dfs(image, r-1, c, color, newColor)
		}
		if c >= 1 {
			dfs(image, r, c-1, color, newColor)
		}
		if r+1 < len(image) {
			dfs(image, r+1, c, color, newColor)
		}
		if c+1 < len(image[0]) {
			dfs(image, r, c+1, color, newColor)
		}
	}
}
