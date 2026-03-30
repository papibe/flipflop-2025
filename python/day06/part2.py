import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


Speed = namedtuple("Speed", ["x_step", "y_step"])

def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    speeds = []

    for line in data:
        values: List[str] = line.split(",")
        x_step: int = int(values[0])
        y_step: int = int(values[1])
        speeds.append(Speed(x_step, y_step))

    return speeds


def solve(speeds: List[str]) -> int:
    n_birds: int = 0

    for picture in range(1, 1_000 + 1):

        for x_step, y_step in speeds:
            x_final: int = (x_step * 3_600 * picture) % 1_000
            y_final: int = (y_step * 3_600 * picture) % 1_000

            if 250 <= x_final <= 749 and 250 <= y_final <= 749:
                n_birds += 1

    return n_birds


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    # print(solution("./example.txt"))  # 0
    print(solution("./input.txt"))  # 137200
