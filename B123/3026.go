package main

import (
	"fmt"
	"math"
)

func psa(prefixSum []int, l, r int) int64 {
	if l > r {
		l, r = r, l
	}

	if l == 0 {
		return int64(prefixSum[r])
	} else {
		return int64(prefixSum[r] - prefixSum[l-1])
	}
}

func maximumSubarraySum(nums []int, k int) int64 {
	mxSum := int64(math.MinInt64 + 1)
	prefixSum := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		if i == 0 {
			prefixSum[i] = nums[i]
		} else {
			prefixSum[i] = prefixSum[i-1] + nums[i]
		}
	}

	mp := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		l, ok := mp[nums[i]-k]
		if ok {
			if psa(prefixSum, l, i) > mxSum {
				mxSum = psa(prefixSum, l, i)
			}
		}

		r, ok := mp[nums[i]+k]
		if ok {
			if psa(prefixSum, r, i) > mxSum {
				mxSum = psa(prefixSum, r, i)
			}
		}

		val, ok := mp[nums[i]]
		if !ok || prefixSum[i] <= prefixSum[val] {
			mp[nums[i]] = i
		}
	}

	if mxSum == math.MinInt64+1 {
		return 0
	}
	return mxSum
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6}
	k := 1
	fmt.Println(maximumSubarraySum(nums, k))
}
