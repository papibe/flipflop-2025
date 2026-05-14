package main

import (
	"cmp"
	"fmt"
	"os"
	"slices"
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

	for _, grid := range grids {
		x := grid.rows - 1
		y := grid.cols - 1
		z := x

		// Custom sort: Descending order
		numbers := []int{x, y, z}
		slices.SortFunc(numbers, func(a, b int) int {
			return cmp.Compare(b, a) // Swapping a and b gives descending order
		})
		x = numbers[0]
		y = numbers[1]
		z = numbers[2]

		paths := factorial_n_over_m(x+y+z, x) / (factorial(y) * factorial(z))
		total_sum += paths
	}
	return total_sum
}

func solution(filename string) int {
	grids := parse(filename)
	return solve(grids)
}

func main() {
	fmt.Println(solution("./example.txt")) // 108
	fmt.Println(solution("./input.txt"))   // 4079922
}
