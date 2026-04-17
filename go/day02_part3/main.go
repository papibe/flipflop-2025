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
	n := len(data)

	index := 0
	for index < n {
		j := index
		counter := 0
		for j < n && data[j] == data[index] {
			j += 1
			counter += 1
		}

		if data[index] == UP {
			height += fibonacci(counter)

		} else if data[index] == DOWN {
			height -= fibonacci(counter)

		}

		max_height = max(max_height, height)
		index = j
	}

	return max_height
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example3.txt")) // 5
	fmt.Println(solution("./example2.txt")) // 4
	fmt.Println(solution("./example4.txt")) // 144
	fmt.Println(solution("./input.txt"))    // 49475
}
