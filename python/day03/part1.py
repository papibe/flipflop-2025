from typing import Dict, List


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def solve(data: List[str]) -> str:
    colors: Dict[str, int] = {}
    max_appearances: int = 0
    max_color: str = ""

    for color in data:
        colors[color] = colors.get(color, 0) + 1

        if colors[color] > max_appearances:
            max_appearances = colors[color]
            max_color = color

    return max_color


def solution(filename: str) -> str:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # "10,20,30"
    print(solution("./input.txt"))  # "27,73,88"
