package main

func vowel(c rune) bool {
	if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
		return true
	} else {
		return false
	}
}

func beautifulSubstrings(s string, k int) int64 {
	n, cnt := len(s), 0
	vw, cn := make([]int, n), make([]int, n)

	if vowel(rune(s[0])) {
		vw[0] = 1
	} else {
		cn[0] = 1
	}

	for i := 1; i < n; i++ {
		if vowel(rune(s[i])) {
			vw[i] = vw[i-1] + 1
			cn[i] = cn[i-1]
		} else {
			cn[i] = cn[i-1] + 1
			vw[i] = vw[i-1]
		}
	}

	for i := 1; i < n/2; i++ {
		if i*i % k == 0 {
			
		}
	}
}
