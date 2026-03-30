import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


Coords = namedtuple("Coords", ["x", "y"])


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    trash_bags = []

    for line in data:
        split_line: List[str] = line.split(",")
        trash_bags.append(Coords(int(split_line[0]), int(split_line[1])))

    return trash_bags


def solve(trash_bags: List[str]) -> int:
    current_x: int = 0
    current_y: int = 0
    steps: int = 0

    for x, y in trash_bags:
        steps += max(abs(current_x - x), abs(current_y - y))
        current_x = x
        current_y = y

    return steps


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 0
