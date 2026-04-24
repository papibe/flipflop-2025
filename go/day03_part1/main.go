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

func solve(data []string) string {
	colors := make(map[string]int)
	max_appearances := 0
	max_color := ""

	for _, color := range data {
		value, is_in_color := colors[color]
		if !is_in_color {
			value = 0
		}
		colors[color] = value + 1

		if colors[color] > max_appearances {
			max_appearances = colors[color]
			max_color = color
		}
	}
	return max_color
}

func solution(filename string) string {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example.txt")) // "10,20,30"
	fmt.Println(solution("./input.txt"))   // "27,73,88"
}
