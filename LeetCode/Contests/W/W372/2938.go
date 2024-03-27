package main

func minimumSteps(s string) int64 {
	nums := make([]int, len(s))
	b, w := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			nums[i] = 1
			b++
		} else {
			nums[i] = 0
			w++
		}
	}

	ip := 0
	var v []int
	var ret int64

	ret = 0

	for i := w; i < len(s); i++ {
		if nums[i] == 1 {
			ip++
		} else {
			v = append(v, i)
		}
	}

	j := 0
	for i := 0; i < w; i++ {
		if nums[i] == 1 {
			ret += int64(v[j] - i)
			j++
		}
	}
	return ret
}
