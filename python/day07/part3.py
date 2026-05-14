from collections import namedtuple
from math import factorial
from typing import List

Grid = namedtuple("Grid", ["dimensions", "size"])


def parse(filename: str) -> List[Grid]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    grids: List[Grid] = []
    for line in data:
        values: List[str] = line.split()
        dimensions: int = int(values[0])
        size: int = int(values[1])
        grids.append(Grid(dimensions, size))

    return grids


def solve(grids: List[Grid]) -> int:
    total_sum: int = 0

    for dimensions, size in grids:
        n: int = (size - 1) * (dimensions)
        paths = factorial(n) // (factorial(size - 1) ** (dimensions))
        total_sum += paths

    return total_sum


def solution(filename: str) -> int:
    data: List[Grid] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 99
    print(solution("./example2.txt"))  # 2520
    print(solution("./input.txt"))  # 455219065224
