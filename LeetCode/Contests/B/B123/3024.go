package main

import (
	"fmt"
)

func triangleType(nums []int) string {
    a, b, c := nums[0], nums[1], nums[2]

	if a+b <= c || a+c <= b || b+c <= a {
		return "none"
	}

	if a == b && b == c {
		return "equilateral"
	}

	if a == b && b != c || a == c && c != b || b == c && c != a {
		return "isosceles"
	}
	
	if a != b && b != c && a != c {
		return "scalene"
	}

	return ""
}

// func main () {
// 	nums := []int{3, 4, 7}
// 	fmt.Println(triangleType(nums))
// }