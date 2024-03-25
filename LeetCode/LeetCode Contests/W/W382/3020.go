package main

import (
	"fmt"
	"sort"
)

func maximumLength(nums []int) int {
	mp := make(map[int]int)

	for _, i := range nums {
		mp[i]++
	}

	fmt.Println(mp)

	ans := 0

	keys := make([]int, 0, len(mp))

	for k := range mp {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	for _, key := range keys {

		t, cnt := key, 0

		if t == 1 {
			cnt += mp[1]
			mp[1] = 0

			if cnt%2 == 0 {
				cnt--
			}

			if cnt > ans {
				ans = cnt
			}

			continue
		}

		for {
			if t > 1e15 || mp[t] <= 0 {
				break
			}

			cnt += 2

			if mp[t] == 1 {
				break
			}

			mp[t] = 0
			t = t * t

			// fmt.Printf("was here %d %d\n", t, mp[t])
		}

		if cnt%2 == 0 {
			cnt--
		}

		if cnt > ans {
			ans = cnt
		}
	}
	return ans
}

func main() {
	nums := []int{14, 14, 196, 196, 38416, 38416}

	ans := maximumLength(nums)
	fmt.Println(ans)
}
