package main

import (
	"fmt"
)

func isInside(points [][]int, tx, ty, bx, by int) bool {
	for i := 0; i < len(points); i++ {
		x, y := points[i][0], points[i][1]

		if x == tx && y == ty || x == bx && y == by {
			continue
		}

		if x <= bx && x >= tx && y <= ty && y >= by {
			return true
		}
	}
	return false 
}

func numberOfPairs(points [][]int) int {
	cnt := 0
    for i := 0; i < len(points); i++ {
		tx, ty := points[i][0], points[i][1]

		for j := 0; j < len(points); j++ {
			bx, by := points[j][0], points[j][1]

			if bx == tx && by == ty {
				continue
			}

			if bx < tx || by > ty {
				continue
			}

			if !isInside(points, tx, ty, bx, by) {
				cnt++

				fmt.Printf("(%d, %d) (%d, %d)\n", tx, ty, bx, by)
			}
		}
	}
	return cnt
}

// func main () {
// 	pts := [][]int {
// 		{3, 1},
// 		{1, 3},
// 		{1, 1},
// 	}
// 	fmt.Println(numberOfPairs(pts))
// }