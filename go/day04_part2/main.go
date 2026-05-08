package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type TrashBag struct {
	x int
	y int
}

func parse(filename string) []TrashBag {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	trash_bags := []TrashBag{}
	for _, line := range lines {
		split_line := strings.Split(line, ",")
		x, _ := strconv.Atoi(split_line[0])
		y, _ := strconv.Atoi(split_line[1])
		trash_bags = append(trash_bags, TrashBag{x, y})
	}

	return trash_bags
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func solve(trash_bags []TrashBag) int {
	current_x, current_y := 0, 0
	steps := 0

	for _, bag := range trash_bags {
		steps += max(abs(current_x-bag.x), abs(current_y-bag.y))
		current_x, current_y = bag.x, bag.y
	}
	return steps
}

func solution(filename string) int {
	trash_bags := parse(filename)
	return solve(trash_bags)
}

func main() {
	fmt.Println(solution("./example.txt")) // 12
	fmt.Println(solution("./input.txt"))   // 4817
}
