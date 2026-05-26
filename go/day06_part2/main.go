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
	n_birds := 0

	for picture := 1; picture <= 1000; picture++ {

		for _, speed := range speeds {
			x_final := mod(speed.x_step*3600*picture, 1000)
			y_final := mod(speed.y_step*3600*picture, 1000)

			if 251 <= x_final && x_final <= 749 && 251 <= y_final && y_final <= 749 {
				n_birds++
			}
		}

	}
	return n_birds
}

func solution(filename string) int {
	speeds := parse(filename)
	return solve(speeds)
}

func main() {
	fmt.Println(solution("./input.txt")) // 137200
}
