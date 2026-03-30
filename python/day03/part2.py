from collections import namedtuple
from typing import List

Color = namedtuple("Color", ["red", "green", "blue"])


def parse(filename: str) -> List[Color]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    colors: List[Color] = []
    for line in data:
        split_line = line.split(",")
        red: int = int(split_line[0])
        green: int = int(split_line[1])
        blue: int = int(split_line[2])

        colors.append(Color(red, green, blue))

    return colors


def solve(colors: List[Color]) -> int:
    reds = greens = blues = specials = 0

    for red, green, blue in colors:
        if red == green or red == blue or green == blue:
            specials += 1

        elif red > green and red > blue:
            reds += 1

        elif green > red and green > blue:
            greens += 1

        elif blue > red and blue > green:
            blues += 1

    return greens


def solution(filename: str) -> int:
    data: List[Color] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 764
