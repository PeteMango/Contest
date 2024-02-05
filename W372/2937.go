package main

import (
	"math"
)

func min(a, b, c int) int {
	return int(math.Min(math.Min(float64(a), float64(b)), float64(c)))
}

func findMinimumOperations(s1 string, s2 string, s3 string) int {
	cnt, min := 0, min(len(s1), len(s2), len(s3))

	if s1 == s2 && s2 == s3 {
		return 0
	}

	for i := 0; i < min; i++ {
		if s1[i] != s2[i] || s1[i] != s3[i] || s2[i] != s3[i] {
			break
		} else {
			cnt++
		}
	}
	if cnt < 2 {
		if s1[0] == s2[0] && s2[0] == s3[0] {
			return (len(s1) - cnt) + (len(s2) - cnt) + (len(s3) - cnt)
		} else {
			return -1
		}
	}
	return (len(s1) - cnt) + (len(s2) - cnt) + (len(s3) - cnt)
}
