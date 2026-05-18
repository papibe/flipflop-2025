package main

import (
	"fmt"
	"os"
	"strings"
)

type Tunnel struct {
	entrance int
	exit     int
}

func parse(filename string) (string, map[rune]*Tunnel) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	line := strings.Trim(string(data), "\n")
	tunnels := make(map[rune]*Tunnel)

	for index, char := range line {
		_, char_in_tunnels := tunnels[char]
		if !char_in_tunnels {
			tunnels[char] = &Tunnel{index, 0}
		} else {
			tunnels[char].exit = index
		}
	}

	return line, tunnels
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func solve(data string, tunnels map[rune]*Tunnel) string {
	index := 0
	steps := 0

	visited := make(map[rune]bool)

	for index < len(data) {
		tunnel := rune(data[index])
		visited[tunnel] = true
		entrance := tunnels[tunnel].entrance
		exit := tunnels[tunnel].exit

		var exit_index int
		if index == exit {
			exit_index = entrance
		} else {
			exit_index = exit
		}
		steps += abs(exit_index - index)
		index = exit_index + 1
	}

	not_visited := []rune{}
	seen := make(map[rune]bool)
	for _, tunnel := range data {
		_, tunnel_is_visited := visited[tunnel]
		_, seen_before := seen[tunnel]

		if !seen_before && !tunnel_is_visited {
			not_visited = append(not_visited, tunnel)
			seen[tunnel] = true
		}
	}

	return string(not_visited)
}

func solution(filename string) string {
	data, tunnels := parse(filename)
	return solve(data, tunnels)
}

func main() {
	fmt.Println(solution("./example.txt")) // "Bc"
	fmt.Println(solution("./input.txt"))   // "eBnXhWDRUCbVZw"
}
