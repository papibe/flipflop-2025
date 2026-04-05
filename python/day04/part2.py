from collections import namedtuple
from typing import List

TrashBag = namedtuple("TrashBag", ["x", "y"])


def parse(filename: str) -> List[TrashBag]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    trash_bags = []

    for line in data:
        split_line: List[str] = line.split(",")
        trash_bags.append(TrashBag(int(split_line[0]), int(split_line[1])))

    return trash_bags


def solve(trash_bags: List[TrashBag]) -> int:
    current_x: int = 0
    current_y: int = 0
    steps: int = 0

    for x, y in trash_bags:
        steps += max(abs(current_x - x), abs(current_y - y))
        current_x = x
        current_y = y

    return steps


def solution(filename: str) -> int:
    trash_bags: List[TrashBag] = parse(filename)
    return solve(trash_bags)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 12
    print(solution("./input.txt"))  # 4817
