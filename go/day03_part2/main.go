package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Color struct {
	red   int
	green int
	blue  int
}

func parse(filename string) []Color {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	colors := []Color{}

	for _, line := range strings.Split(strings.Trim(string(data), "\n"), "\n") {
		split_line := strings.Split(line, ",")
		red, _ := strconv.Atoi(split_line[0])
		green, _ := strconv.Atoi(split_line[1])
		blue, _ := strconv.Atoi(split_line[2])

		colors = append(colors, Color{red, green, blue})
	}
	return colors
}

func solve(colors []Color) int {
	reds, greens, blues, specials := 0, 0, 0, 0

	for _, color := range colors {
		red, green, blue := color.red, color.green, color.blue

		if red == green || red == blue || green == blue {
			specials += 1
		} else if red > green && red > blue {
			reds += 1
		} else if green > red && green > blue {
			greens += 1
		} else if blue > red && blue > green {
			blues += 1
		}
	}

	return greens
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./example.txt")) // 0
	fmt.Println(solution("./input.txt"))   // 764
}
