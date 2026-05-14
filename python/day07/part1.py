from collections import namedtuple
from math import factorial
from typing import List

Grid = namedtuple("Grid", ["row", "cols"])


def parse(filename: str) -> List[Grid]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    grids: List[Grid] = []
    for line in data:
        values: List[str] = line.split()
        rows: int = int(values[0])
        cols: int = int(values[1])
        grids.append(Grid(rows, cols))

    return grids


def solve(grids: List[Grid]) -> int:
    total_sum: int = 0

    for rows, cols in grids:
        n: int = rows + cols - 2
        paths: int = factorial(n) // (factorial(cols - 1) * factorial(rows - 1))
        total_sum += paths

    return total_sum


def solution(filename: str) -> int:
    data: List[Grid] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 11
    print(solution("./input.txt"))  # 221
