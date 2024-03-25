package main

import (
	"fmt"
	"strings"
)

func longestEquivalentPreSuffix(s string, k int) int {
	n, start := len(s), 0

	start = n - k

	fmt.Printf("the start is %d\n", start)

	for length := start; length >= 0; length-- {
		if (n-length)%k != 0 {
			continue
		}

		prefix := s[:length]
		if strings.HasSuffix(s, prefix) {
			return len(prefix)
		}
	}
	return 0
}

func minimumTimeToInitialState(word string, k int) int {
	length, n := longestEquivalentPreSuffix(word, k), len(word)

	if n == k {
		return 1
	}

	fmt.Printf("length is %d\n", length)

	if length > n-k {
		length = n - k
	}

	rest := n - length

	if rest%k == 0 {
		return rest / k
	} else {
		return (rest / k) + 1
	}
}
