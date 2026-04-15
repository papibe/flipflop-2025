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

func solve(data string) int {
	height := 0
	max_height := 0

	for _, char := range data {
		if char == UP {
			height += 1
		} else if char == DOWN {
			height -= 1
		}
		max_height = max(max_height, height)
	}

	return max_height
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example1.txt")) // 1
	fmt.Println(solution("./example2.txt")) // 6
	fmt.Println(solution("./input.txt"))    // 145
}
