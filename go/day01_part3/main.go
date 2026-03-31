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
		points := strings.Count(banana, "ne")
		if points > 0 {
			continue
		}
		points += strings.Count(banana, "ba")
		points += strings.Count(banana, "na")

		total_sum += points
	}
	return total_sum
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example.txt")) // 16
	fmt.Println(solution("./input.txt"))   // 5250
}
