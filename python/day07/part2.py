import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple
from math import factorial


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    grids = []
    for line in data:
        values: List[str] = line.split()
        rows: int = int(values[0])
        cols: int = int(values[1])
        grids.append((rows, cols))

    return grids


def solve(grids: List[str]) -> int:
    total_sum: int = 0

    for rows, cols in grids:
        x: int = rows - 1
        y: int = cols - 1
        z: int  = x
        paths = factorial(x + y + z) // (factorial(x) * factorial(y) * factorial(z))
        total_sum += paths
        print(rows, cols, paths)

    return total_sum


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 11
    print(solution("./input.txt"))  # 221
