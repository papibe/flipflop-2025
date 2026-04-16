package main

import (
	"fmt"
	"os"
	"strings"
)

const UP = '^'
const DOWN = 'v'

func parse(filename string) string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	return strings.Trim(string(data), "\n")
}

var memo = map[int]int{}

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	cached_value, in_memo := memo[n]
	if in_memo {
		return cached_value
	}

	memo[n] = fibonacci(n-1) + fibonacci(n-2)
	return memo[n]
}

func solve(data string) int {
	height := 0
	max_height := 0
	repetitions := 0
	previous := '\x00'

	for _, char := range data {
		if char == previous {
			repetitions += 1
		} else {
			repetitions = 1
		}

		if char == UP {
			height += repetitions
		} else if char == DOWN {
			height -= repetitions
		}

		max_height = max(max_height, height)
		previous = char
	}

	return max_height
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example3.txt")) // 15
	fmt.Println(solution("./example2.txt")) // 15
	fmt.Println(solution("./input.txt"))    // 1971
}
