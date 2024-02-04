package main

import (
	"fmt"
)

func cr(a, b, threshold int) bool {
	if a > b {
		if a-b > threshold {
			return false
		}
		return true
	} else {
		if b-a > threshold {
			return false
		}
		return true
	}
}

/*
a b c
d e f
g h i
*/

func applyThreshold(region, count [][]int, image [][]int, threshold, x, y int) {
	if x+2 >= len(image) || y+2 >= len(image[0]) {
		return
	}

	a, b, c := image[x][y], image[x][y+1], image[x][y+2]
	d, e, f := image[x+1][y], image[x+1][y+1], image[x+1][y+2]
	g, h, i := image[x+2][y], image[x+2][y+1], image[x+2][y+2]

	if !cr(a, b, threshold) || !cr(a, d, threshold) || !cr(b, c, threshold) || !cr(b, e, threshold) ||
		!cr(c, f, threshold) || !cr(d, e, threshold) || !cr(d, g, threshold) || !cr(e, f, threshold) ||
		!cr(e, h, threshold) || !cr(f, i, threshold) || !cr(g, h, threshold) || !cr(h, i, threshold) {
		return
	}

	// fmt.Println("changing")

	average := int((a + b + c + d + e + f + g + h + i) / 9)
	for dx := 0; dx < 3; dx++ {
		for dy := 0; dy < 3; dy++ {
			regionX, regionY := x+dx, y+dy
			region[regionX][regionY] += average
			count[regionX][regionY]++
		}
	}
}

func resultGrid(image [][]int, threshold int) [][]int {
	rows := len(image)
	cols := len(image[0])

	result := make([][]int, rows)
	region := make([][]int, rows)
	count := make([][]int, rows)

	for i := range result {
		result[i] = make([]int, cols)
	}

	for i := range region {
		region[i] = make([]int, cols)
	}

	for i := range count {
		count[i] = make([]int, cols)
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			result[i][j] = 0
		}
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			count[i][j] = 0
		}
	}

	for i := 0; i <= rows; i++ {
		for j := 0; j <= cols-3; j++ {
			applyThreshold(region, count, image, threshold, i, j)
		}
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if count[i][j] == 0 {
				continue
			}
			region[i][j] /= count[i][j]
		}
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if region[i][j] == 0 {
				result[i][j] = image[i][j]
			} else {
				result[i][j] = region[i][j]
			}
		}
	}

	return result
}

func main() {
	image := [][]int{
		{5, 6, 7, 10},
		{8, 9, 10, 10},
		{11, 12, 13, 10},
	}
	threshold := 3

	// Find the grid of region average
	result := resultGrid(image, threshold)

	// Print the result
	for _, row := range result {
		for _, val := range row {
			fmt.Printf("%d ", val)
		}
		fmt.Println()
	}
}
