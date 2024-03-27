package main

import (
	"math"
)

func countKeyChanges(s string) int {
	cnt := 0
	for i := 1; i < len(s); i++ {
		prev, cur := s[i-1], s[i]

		prevAscii, curAscii := float64(prev-'0'), float64(cur-'0')
		if math.Abs(prevAscii-curAscii) != 32 && prevAscii != curAscii {
			// fmt.Printf("%c %c", prev, cur)
			cnt++
		}
	}
	return cnt
}
