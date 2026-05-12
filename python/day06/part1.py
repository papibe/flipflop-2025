from collections import namedtuple
from typing import List, Tuple

Speed = namedtuple("Speed", ["x_step", "y_step"])


def parse(filename: str) -> List[Speed]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    speeds = []

    for line in data:
        values: List[str] = line.split(",")
        x_step: int = int(values[0])
        y_step: int = int(values[1])
        speeds.append(Speed(x_step, y_step))

    return speeds


def solve(speeds: List[Speed]) -> int:
    positions: List[Tuple[int, int]] = []

    for x_step, y_step in speeds:
        x_final: int = (x_step * 100) % 1_000
        y_final: int = (y_step * 100) % 1_000
        positions.append((x_final, y_final))

    n_birds: int = 0
    # take picture
    for x_final, y_final in positions:
        if 251 <= x_final <= 749 and 251 <= y_final <= 749:
            n_birds += 1

    return n_birds


def solution(filename: str) -> int:
    speeds: List[Speed] = parse(filename)
    return solve(speeds)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 260
