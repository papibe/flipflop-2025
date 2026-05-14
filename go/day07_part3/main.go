package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Grid struct {
	dimensions int
	size       int
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
		dimensions, _ := strconv.Atoi(values[0])
		size, _ := strconv.Atoi(values[1])
		grids = append(grids, Grid{dimensions, size})
	}

	return grids
}

func factorial_n_over_m(n, m int) int {
	result := 1
	for i := n; i > m; i-- {
		result *= i
	}
	return result
}

func factorial(n int) int {
	return factorial_n_over_m(n, 1)
}

func solve(grids []Grid) int {
	total_sum := 0
	const MaxInt = int(^uint(0) >> 1)
	// const MinInt = -MaxInt - 1

	for _, grid := range grids {
		n := (grid.size - 1) * (grid.dimensions)
		paths := factorial(n) / int(math.Pow(float64(factorial(grid.size-1)), float64(grid.dimensions)))
		total_sum += paths
	}
	return total_sum
}

func solution(filename string) int {
	grids := parse(filename)
	return solve(grids)
}

func main() {
	fmt.Println(solution("./example1.txt")) // 98
	fmt.Println(solution("./example2.txt")) // 2520
	fmt.Println(solution("./input.txt"))    // 455219065224
}
