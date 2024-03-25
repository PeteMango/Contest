package main

import "fmt"

func areSimilar(mat [][]int, k int) bool {
	rows := len(mat)
	if rows == 0 {
		return true
	}
	cols := len(mat[0])
	shiftRow := func(row []int, k int) {
		realK := k % len(row)
		if realK == 0 {
			return
		}
		copy(row, append(row[len(row)-realK:], row[:len(row)-realK]...))
	}

	// Perform the cyclic shifts
	for i, row := range mat {
		if (i%2 == 0 && k%2 == 1) || (i%2 == 1 && k%2 == 0) {
			shiftRow(row, k)
		}
	}

	for i, row := range mat {
		for j, val := range row {
			if val != mat[(i+k)%rows][(j+k)%cols] {
				return false
			}
		}
	}

	return true
}

func main() {
	mat := [][]int{{1, 2, 1, 2}, {5, 5, 5, 5}, {6, 3, 6, 3}}
	k := 2
	fmt.Println(areSimilar(mat, k))
}
