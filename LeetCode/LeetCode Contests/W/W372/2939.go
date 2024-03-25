package main

import (
	"fmt"
)

func maximumXorProduct(a int64, b int64, k int) int {
	var MOD int64 = 1e9 + 7
	if a > b {
		a, b = b, a
	}

	var set int64 = 0
	var index int = 49
	for ; index >= 0; index-- {
		var bitx, bity int64 = a & int64(1<<index), b & int64(1<<index)
		if bitx > 0 && bity > 0 {
			continue
		} else if bitx > 0 || bity > 0 {
			break
		}
	}

	for i := k - 1; i >= 0; i-- {
		var bitx, bity int64 = a & int64(1<<i), b & int64(1<<i)
		if bitx == 0 && bity == 0 || bitx == 0 && i != index {
			set += int64(1 << i)
		}
	}

	fmt.Println(set)

	var ret int64 = 0

	ret = (((a ^ set) % MOD) * ((b ^ set) % MOD)) % MOD
	return int(ret)
}

func main() {
	var a, b int64 = 53449611838892, 712958946092406
	var n int = 6
	fmt.Println(maximumXorProduct(a, b, n))
}
