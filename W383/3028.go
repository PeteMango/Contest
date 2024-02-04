package main

func returnToBoundaryCount(nums []int) int {
	cnt, curPos := 0, 0
	for i := 0; i < len(nums); i++ {
		curPos = curPos + nums[i]
		if curPos == 0 {
			cnt++
		}
	}
	return cnt
}
