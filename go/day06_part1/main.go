package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Speed struct {
	x_step int
	y_step int
}

type Position struct {
	x int
	y int
}

func parse(filename string) []Speed {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	speeds := []Speed{}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	for _, line := range lines {
		values := strings.Split(line, ",")
		x_step, _ := strconv.Atoi(values[0])
		y_step, _ := strconv.Atoi(values[1])
		speeds = append(speeds, Speed{x_step, y_step})
	}

	return speeds
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func solve(speeds []Speed) int {
	positions := []Position{}
	for _, speed := range speeds {
		x_final := mod(speed.x_step*100, 1000)
		y_final := mod(speed.y_step*100, 1000)
		positions = append(positions, Position{x_final, y_final})
	}

	n_birds := 0
	for _, position := range positions {
		if 251 <= position.x && position.x <= 749 && 251 <= position.y && position.y <= 749 {
			n_birds++
		}
	}
	return n_birds
}

func solution(filename string) int {
	speeds := parse(filename)
	return solve(speeds)
}

func main() {
	fmt.Println(solution("./input.txt")) // 260
}
