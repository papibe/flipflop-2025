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
        dimensions: int = int(values[0])
        size: int = int(values[1])
        grids.append((dimensions, size))

    return grids


def solve(grids: List[str]) -> int:
    total_sum: int = 0

    # grids.append((4, 3))

    for dimensions, size in grids:

        n: int = (size - 1) * (dimensions)
        paths = factorial(n)// (factorial(size - 1)**(dimensions))
        total_sum += paths
        print(dimensions, size, paths)

    return total_sum


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 99
    print(solution("./input.txt"))  # 221
