package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Grid struct {
	rows int
	cols int
}

func parse(filename string) []Grid {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")
	grids := []Grid{}

	for _, line := range lines {
		values := strings.Split(line, " ")
		rows, _ := strconv.Atoi(values[0])
		cols, _ := strconv.Atoi(values[1])
		grids = append(grids, Grid{rows, cols})
	}

	return grids
}

func factorial(n int) int {
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result
}

func solve(grids []Grid) int {
	total_sum := 0

	for _, grid := range grids {
		n := grid.rows + grid.cols - 2
		paths := factorial(n) / (factorial(grid.cols-1) * factorial(grid.rows-1))
		total_sum += paths
	}
	return total_sum
}

func solution(filename string) int {
	grids := parse(filename)
	return solve(grids)
}

func main() {
	fmt.Println(solution("./example.txt")) // 11
	fmt.Println(solution("./input.txt"))   // 221
}
