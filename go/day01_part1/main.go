package main

import (
	"fmt"
	"os"
	"strings"
)

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func solve(data []string) int {
	total_sum := 0

	for _, banana := range data {
		total_sum += strings.Count(banana, "ba")
		total_sum += strings.Count(banana, "na")
		total_sum += strings.Count(banana, "ne")
	}
	return total_sum
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example.txt")) // 24
	fmt.Println(solution("./input.txt"))   // 10459
}
